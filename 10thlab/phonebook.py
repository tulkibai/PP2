import pg8000  # чисто‑питоновый драйвер для PostgreSQL
import csv

# создаёт базу данных target_db, если её нет
def ensure_database(target_db, db_user, db_password, db_host, db_port):
    # подключаемся к служебной базе postgres для управления БД
    conn = pg8000.connect(
        user=db_user,
        password=db_password,
        database="postgres",
        host=db_host,
        port=int(db_port)
    )
    conn.autocommit = True  # для выполнения CREATE DATABASE вне транзакции
    cursor = conn.cursor()

    # проверяем, существует ли база в системной таблице
    cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s", (target_db,))
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f"CREATE DATABASE {target_db}")  # создаём новую БД
        print(f"База данных '{target_db}' успешно создана.")
    else:
        print(f"База данных '{target_db}' уже существует.")
    cursor.close()
    conn.close()

# подключаемся к целевой базе phonebook_db
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

# создаём таблицу phonebook, если её нет
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
    print("Таблица phonebook создана (если её не было).")

# читаем CSV и вставляем данные в таблицу
def insert_from_csv(cursor, conn, csv_path):
    with open(csv_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) != 3:
                continue  # пропускаем некорректные строки
            first_name, last_name, phone = row
            cursor.execute(
                "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
                (first_name, last_name, phone)
            )
    conn.commit()
    print("Данные из CSV успешно добавлены.")

# вставляем одну запись из консоли
def insert_from_console(cursor, conn):
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    cursor.execute(
        "INSERT INTO phonebook (first_name, last_name, phone) VALUES (%s, %s, %s)",
        (first_name, last_name, phone)
    )
    conn.commit()
    print("Данные добавлены из консоли.")

# обновляем запись на нужное значение
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
    print("Запись обновлена.")

# выборка записей с фильтром или без
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
        print("Нет записей.")

# удаляем запись по указанному полю
def delete_record(cursor, conn):
    print("Delete Record:")
    column = input("Delete by column (first_name/last_name/phone): ").lower()
    value = input(f"Value for {column}: ")
    cursor.execute(
        f"DELETE FROM phonebook WHERE {column} = %s", (value,)
    )
    conn.commit()
    print("Запись(и) удалены.")

# главная функция: создаём БД, таблицу и запускаем меню
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
            break
        else:
            print("Invalid choice.")
    cursor.close()
    conn.close()
    print("Exiting PhoneBook.")

if __name__ == "__main__":
    main()
