import psycopg2


try:
    #подключение к бд
    conn = psycopg2.connect(dbname="bank", user="postgres", password="1234", host="localhost", port="5432")

    #создание курсора
    cursor = conn.cursor()

    #отключаем автокоммит (обязательно его отключать?)
    conn.autocommit = False

    #вставка данных
    cursor.execute("INSERT INTO bank_accounts (account_id, balance) VALUES (1234, 1000.00) ")
    cursor.execute("INSERT INTO bank_accounts (account_id, balance) VALUES (007, 7000.00) ")

    #обновление данных
    cursor.execute("UPDATE bank_accounts SET balance = 5555.55 WHERE account_id = 007")

    #удаление счёта
    cursor.execute("DELETE from bank_accounts WHERE account_id = 1234")

    #сохраняем
    conn.commit()
    print("Транзакция удалась")

#любая ошибка и откатываемся
except Exception as e:
    print(f"Ошибка {e}")
    conn.rollback()

#закрываем курсор и закрываем соединение
finally:
    cursor.close()
    conn.close()
