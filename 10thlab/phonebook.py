import psycopg2
import csv
from psycopg2 import sql

def ensure_database(dbname, user, password, host, port):
    """
    Подключается к служебной базе 'postgres', проверяет,
    существует ли БД dbname, и если нет – создаёт её.
    """
    # Сначала подключимся к служебной базе, где точно есть pg_database
    conn = psycopg2.connect(
        dbname="postgres",  # служебная БД PostgreSQL
        user=user,
        password=password,
        host=host,
        port=port
    )
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Проверяем, есть ли уже такая база
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (dbname,))
    exists = cursor.fetchone()
    
    if not exists:
        # Создаём базу, если её нет
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        print(f"База данных '{dbname}' успешно создана.")
    else:
        print(f"База данных '{dbname}' уже существует.")
    
    cursor.close()
    conn.close()

def connect_db():
    """
    Подключаемся к уже существующей (или только что созданной) БД dbname
    и возвращаем кортеж (connection, cursor).
    """
    conn = psycopg2.connect(
        dbname="phonebook_db",  # <-- Укажите здесь вашу целевую БД
        user="postgres",        # <-- ваш пользователь
        password="123",    # <-- ваш пароль
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, conn):
    create_table_query = """
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(50),
            last_name VARCHAR(50),
            phone VARCHAR(20)
        );
    """
    cursor.execute(create_table_query)
    conn.commit()
    print("Таблица phonebook создана (если её не было).")

def insert_from_csv(cursor, conn, csv_path):
    with open(csv_path, 'r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # Каждый ряд: [first_name, last_name, phone]
            if len(row) != 3:
                continue  # пропускаем некорректные строки
            first_name, last_name, phone = row
            cursor.execute("""
                INSERT INTO phonebook (first_name, last_name, phone)
                VALUES (%s, %s, %s);
            """, (first_name, last_name, phone))

    conn.commit()
    print("Данные из CSV успешно добавлены.")

def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    
    cursor.execute("""
        INSERT INTO phonebook (first_name, last_name, phone)
        VALUES (%s, %s, %s);
    """, (first_name, last_name, phone))
    
    conn.commit()
    print("Данные добавлены из консоли.")

def update_record(cursor, conn):
    print("Update Record:")
    search_column = input("Which column will you use to find the record? (first_name/last_name/phone): ").lower()
    search_value = input("Enter the value to find the record: ")

    update_column = input("Which column do you want to update? (first_name/last_name/phone): ").lower()
    new_value = input(f"Enter the new value for {update_column}: ")

    query = f"""
        UPDATE phonebook
        SET {update_column} = %s
        WHERE {search_column} = %s
    """
    cursor.execute(query, (new_value, search_value))
    conn.commit()

    print("Запись обновлена.")

def query_records(cursor):
    column_to_filter = input("Filter by which column? (first_name/last_name/phone or 'all' for no filter): ").lower()

    if column_to_filter == "all":
        query = "SELECT * FROM phonebook;"
        cursor.execute(query)
    else:
        value = input(f"Enter the value to match in {column_to_filter}: ")
        query = f"SELECT * FROM phonebook WHERE {column_to_filter} = %s;"
        cursor.execute(query, (value,))
    
    rows = cursor.fetchall()

    if rows:
        print("\nQuery Results:")
        for row in rows:
            print(row)
    else:
        print("Нет подходящих записей.")

def delete_record(cursor, conn):
    print("Delete Record:")
    delete_column = input("Delete by which column? (first_name/last_name/phone): ").lower()
    delete_value = input(f"Enter the value of {delete_column}: ")

    query = f"DELETE FROM phonebook WHERE {delete_column} = %s;"
    cursor.execute(query, (delete_value,))
    conn.commit()

    print("Запись(и) успешно удалены.")

def main():
    # 1. Проверяем наличие базы и при необходимости создаём
    ensure_database(
        dbname="phonebook_db",   # <-- та же БД, что указана ниже!
        user="postgres",         # <-- ваш пользователь, имеющий права CREATE DATABASE
        password="postgres",     # <-- ваш пароль
        host="localhost",
        port="5432"
    )
    
    # 2. Подключаемся к уже существующей (или только что созданной) базе
    conn, cursor = connect_db()
    
    # 3. Создаём таблицу phonebook, если её ещё нет
    create_table(cursor, conn)

    # 4. Запускаем меню
    while True:
        print("\n=== PhoneBook Menu ===")
        print("1. Insert data from CSV")
        print("2. Insert data from console")
        print("3. Update record")
        print("4. Query records")
        print("5. Delete record")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            csv_path = input("Enter path to CSV file: ")
            insert_from_csv(cursor, conn, csv_path)
        elif choice == '2':
            insert_from_console(cursor, conn)
        elif choice == '3':
            update_record(cursor, conn)
        elif choice == '4':
            query_records(cursor)
        elif choice == '5':
            delete_record(cursor, conn)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
    
    cursor.close()
    conn.close()
    print("Exiting PhoneBook.")

if __name__ == "__main__":
    main()
