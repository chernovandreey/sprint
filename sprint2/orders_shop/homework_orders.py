import  psycopg2


try:
    conn = psycopg2.connect(dbname = "orders", user = "postgres", password = "1234", host = "localhost", port = "5432")

    cursor = conn.cursor()

    conn.autocommit = False

    cursor.execute("INSERT INTO orders (order_id, customer_id, total_amount) VALUES (1111, 1, 5.8)")

    try:
        cursor.execute("INSERT INTO orders (order_id, total_amount) VALUES (2222, 10.5)")
    except Exception as e:
        print(f"ошибка при добавлении пустого заказа {e}")

    cursor.execute("INSERT INTO orders (order_id, customer_id, total_amount) VALUES (3333, 1, 7.8)")

    conn.commit()
    print("всё чётко")

except Exception as e:
    print(f"Ошибка {e}")
    conn.rollback()
    print("Сделан откат")

finally:
    cursor.close()
    conn.close()
