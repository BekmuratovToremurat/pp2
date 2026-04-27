import psycopg
import csv
from config import DB_HOST, DB_NAME, DB_USER, DB_PASSWORD

# ---------------- DB CONNECTION ----------------

def get_conn():
    return psycopg.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=5432
    )

def execute(query, params=None, fetch=False):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params or ())
            if fetch:
                return cur.fetchall()
            conn.commit()

# ---------------- SETUP ----------------

def create_table():
    execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) UNIQUE NOT NULL,
            email VARCHAR(100),
            birthday DATE,
            group_id INTEGER
        )
    """)

# ---------------- CONTACTS ----------------

def insert_contact(name, email=None, birthday=None, group_id=None):
    execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (name)
        DO UPDATE SET email=EXCLUDED.email
    """, (name, email, birthday, group_id))



def add_phone(name, phone, ptype):
    execute("CALL add_phone(%s, %s, %s)", (name, phone, ptype))
# ---------------- CSV IMPORT ----------------

def insert_from_csv(file):
    with open(file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            insert_contact(
                row["name"],
                row["email"],
                row["birthday"],
                None
            )
    print("CSV imported")

# ---------------- SEARCH ----------------

def search(query):
    return execute("SELECT * FROM search_contacts(%s)", (query,), fetch=True)

# ---------------- PRINT ----------------

def print_rows(rows):
    if not rows:
        print("(empty)")
        return

    for r in rows:
        print(r)

# ---------------- PAGINATION ----------------

def paginate(limit, page):
    offset = limit * page
    return execute("""
        SELECT * FROM contacts
        ORDER BY id
        LIMIT %s OFFSET %s
    """, (limit, offset), fetch=True)

# ---------------- MENU ----------------

def main():
    create_table()

    while True:
        print("""
1. Add contact
2. Import CSV
3. Search
4. Pagination
0. Exit
""")

        choice = input("> ")

        if choice == "1":
            name = input("name: ")
            email = input("email: ")
            birthday = input("birthday: ")

            insert_contact(name, email, birthday)

            phone = input("phone: ")
            ptype = input("type (home/work/mobile): ")

            add_phone(name, phone, ptype)

        elif choice == "2":
            insert_from_csv(input("file: "))

        elif choice == "3":
            print_rows(search(input("query: ")))

        elif choice == "4":
            page = int(input("page: "))
            print_rows(paginate(5, page))

        elif choice == "0":
            break

if __name__ == "__main__":
    main()