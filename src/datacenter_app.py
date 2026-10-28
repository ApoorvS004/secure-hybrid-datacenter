
import os
import psycopg2


def main():
    connection = psycopg2.connect(
        host=os.environ["DB_HOST"],
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        connect_timeout=5,
    )

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, message FROM lab_check;")
            rows = cursor.fetchall()

            print("Connected to the private datacenter database.")
            for row in rows:
                print(f"ID: {row[0]} | Message: {row[1]}")
    finally:
        connection.close()


if __name__ == "__main__":
    main()
