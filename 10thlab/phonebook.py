import pg8000
import csv
import json

# Ensure the database exists
def ensure_database(target_db, db_user, db_password, db_host, db_port):
    conn = pg8000.connect(
        user=db_user,
        password=db_password,
        database="postgres",
        host=db_host,
        port=int(db_port)
    )
    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (target_db,))
    exists = cursor.fetchone()
    if not exists:
        cursor.execute(f"CREATE DATABASE {target_db}")
        print(f"Database '{target_db}' created successfully.")
    else:
        print(f"Database '{target_db}' already exists.")
    cursor.close()
    conn.close()

# Connect to the database
def connect_db():
    conn = pg8000.connect(
        user="postgres",
        password="123",
        database="phonebook_db",
        host="localhost",
        port=5432
    )
    cursor = conn.cursor()
    return conn, cursor

# Create the phonebook table if it doesn't exist
def create_table(cursor, conn):
    create_table_query = (
        "CREATE TABLE IF NOT EXISTS phonebook ("
        "id SERIAL PRIMARY KEY,"
        "first_name VARCHAR(50),"
        "last_name VARCHAR(50),"
        "phone VARCHAR(20)"
        ");"
    )
    cursor.execute(create_table_query)
    conn.commit()
    print("Table phonebook created (if it didn't exist).")

# Create PostgreSQL functions and procedures
def create_functions_and_procedures(cursor):
    commands = [
        """
        CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern TEXT)
        RETURNS SETOF phonebook AS $$
            SELECT * FROM phonebook
            WHERE first_name LIKE '%' || pattern || '%'
               OR last_name LIKE '%' || pattern || '%'
               OR phone LIKE '%' || pattern || '%';
        $$ LANGUAGE sql;
        """,
        """
        CREATE OR REPLACE PROCEDURE insert_or_update_user(
            p_first_name VARCHAR(50),
            p_last_name VARCHAR(50),
            p_phone VARCHAR(20)
        )
        LANGUAGE plpgsql
        AS $$
        BEGIN
            IF EXISTS (SELECT 1 FROM phonebook WHERE first_name = p_first_name AND last_name = p_last_name) THEN
                UPDATE phonebook SET phone = p_phone WHERE first_name = p_first_name AND last_name = p_last_name;
            ELSE
                INSERT INTO phonebook (first_name, last_name, phone) VALUES (p_first_name, p_last_name, p_phone);
            END IF;
        END;
        $$;
        """,
        """
        CREATE OR REPLACE FUNCTION insert_users_bulk(users_json JSON)
        RETURNS JSONB
        LANGUAGE plpgsql
        AS $$
        DECLARE
            user_record JSON;
            first_name VARCHAR(50);
            last_name VARCHAR(50);
            phone VARCHAR(20);
            invalid_users JSONB := '[]'::JSONB;
        BEGIN
            FOR user_record IN SELECT * FROM json_array_elements(users_json)
            LOOP
                first_name := user_record->>'first_name';
                last_name := user_record->>'last_name';
                phone := user_record->>'phone';
                IF phone ~ '^\+\d+$' THEN
                    INSERT INTO phonebook (first_name, last_name, phone)
                    VALUES (first_name, last_name, phone);
                ELSE
                    invalid_users := invalid_users || user_record::JSONB;
                END IF;
            END LOOP;
            RETURN invalid_users;
        END;
        $$;
        """,
        """
        CREATE OR REPLACE FUNCTION get_phonebook_paginated(p_limit INTEGER, p_offset INTEGER)
        RETURNS SETOF phonebook AS $$
            SELECT * FROM phonebook
            ORDER BY id
            LIMIT p_limit OFFSET p_offset;
        $$ LANGUAGE sql;
        """,
        """
        CREATE OR REPLACE PROCEDURE delete_by_pattern(pattern TEXT)
        LANGUAGE plpgsql
        AS $$
        BEGIN
            DELETE FROM phonebook
            WHERE first_name LIKE '%' || pattern || '%'
               OR last_name LIKE '%' || pattern || '%'
               OR phone LIKE '%' || pattern || '%';
        END;
        $$;
        """
    ]
    for command in commands:
        cursor.execute(command)
    print("Functions and procedures created or updated.")

# Insert data from CSV
def insert_from_csv(cursor, conn, csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 3:
                continue
            first_name, last_name, phone = row
            cursor.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (first_name, last_name, phone)
            )
    conn.commit()
    print("Data from CSV inserted successfully.")

# Insert data from console
def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    print("Data inserted from console.")

# Update a record
def update_record(cursor, conn):
    print("Update Record:")
    search_column = input("Column to search by (first_name/last_name/phone): ").lower()
    search_value = input("Value to find: ")
    update_column = input("Column to update (first_name/last_name/phone): ").lower()
    new_value = input(f"New value for {update_column}: ")
    cursor.execute(
        f"UPDATE phonebook SET {update_column} = %s WHERE {search_column} = %s",
        (new_value, search_value)
    )
    conn.commit()
    print("Record updated.")

# Query records
def query_records(cursor):
    column = input("Filter by (first_name/last_name/phone or 'all'): ").lower()
    if column == 'all':
        cursor.execute("SELECT * FROM phonebook")
    else:
        value = input(f"Value for {column}: ")
        cursor.execute(
            f"SELECT * FROM phonebook WHERE {column} = %s", (value,)
        )
    rows = cursor.fetchall()
    if rows:
        print("\nResults:")
        for row in rows:
            print(row)
    else:
        print("No records found.")

# Delete a record
def delete_record(cursor, conn):
    print("Delete Record:")
    column = input("Delete by column (first_name/last_name/phone): ").lower()
    value = input(f"Value for {column}: ")
    cursor.execute(
        f"DELETE FROM phonebook WHERE {column} = %s", (value,)
    )
    conn.commit()
    print("Record(s) deleted.")

# Search records by pattern
def search_by_pattern(cursor):
    pattern = input("Enter search pattern: ")
    cursor.execute("SELECT * FROM get_records_by_pattern(%s)", (pattern,))
    rows = cursor.fetchall()
    if rows:
        print("\nResults:")
        for row in rows:
            print(row)
    else:
        print("No records found.")

# Insert or update a user
def insert_or_update_user(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute("CALL insert_or_update_user(%s, %s, %s)", (first_name, last_name, phone))
    conn.commit()
    print("User inserted or updated.")

# Insert multiple users with validation
def insert_multiple_users(cursor, conn):
    path = input("Path to CSV (columns: first_name, last_name, phone; no headers): ")
    with open(path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        users = [{'first_name': row[0], 'last_name': row[1], 'phone': row[2]} for row in reader if len(row) == 3]
    users_json = json.dumps(users)
    cursor.execute("SELECT insert_users_bulk(%s)", (users_json,))
    invalid_users = cursor.fetchone()[0]
    conn.commit()
    if invalid_users and json.loads(invalid_users):
        print("Invalid users (phone must start with '+' followed by digits):")
        for user in json.loads(invalid_users):
            print(user)
    else:
        print("All users inserted successfully.")

# Query with pagination
def query_with_pagination(cursor):
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cursor.execute("SELECT * FROM get_phonebook_paginated(%s, %s)", (limit, offset))
    rows = cursor.fetchall()
    if rows:
        print("\nResults:")
        for row in rows:
            print(row)
    else:
        print("No records found.")

# Delete by pattern
def delete_by_pattern(cursor, conn):
    pattern = input("Enter pattern to delete: ")
    cursor.execute("CALL delete_by_pattern(%s)", (pattern,))
    conn.commit()
    print("Records deleted.")

# Main function
def main():
    ensure_database(
        target_db="phonebook_db",
        db_user="postgres",
        db_password="123",
        db_host="localhost",
        db_port=5432
    )
    conn, cursor = connect_db()
    create_table(cursor, conn)
    create_functions_and_procedures(cursor)
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Insert data from CSV")
        print("2. Insert data from console")
        print("3. Update record")
        print("4. Query records")
        print("5. Delete record")
        print("6. Search by pattern")
        print("7. Insert or update user")
        print("8. Insert multiple users with validation")
        print("9. Query with pagination")
        print("10. Delete by pattern")
        print("11. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            path = input("Path to CSV: ")
            insert_from_csv(cursor, conn, path)
        elif choice == '2':
            insert_from_console(cursor, conn)
        elif choice == '3':
            update_record(cursor, conn)
        elif choice == '4':
            query_records(cursor)
        elif choice == '5':
            delete_record(cursor, conn)
        elif choice == '6':
            search_by_pattern(cursor)
        elif choice == '7':
            insert_or_update_user(cursor, conn)
        elif choice == '8':
            insert_multiple_users(cursor, conn)
        elif choice == '9':
            query_with_pagination(cursor)
        elif choice == '10':
            delete_by_pattern(cursor, conn)
        elif choice == '11':
            break
        else:
            print("Invalid choice.")
    cursor.close()
    conn.close()
    print("Exiting PhoneBook.")

if __name__ == "__main__":
    main()