import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# Подключение к серверу PostgreSQL
connection = psycopg2.connect(
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# Создание курсора для выполнения запросов
cursor = connection.cursor()

# Имя базы данных, которую нужно удалить
database_name = "bank"

# Выполнение запроса для удаления базы данных
cursor.execute(f"DROP DATABASE {database_name};")


# Закрытие курсора и соединения
cursor.close()
connection.close()
