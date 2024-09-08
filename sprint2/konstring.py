from sqlalchemy import create_engine, MetaData

# создание объекта engine и подключение к базе данных
engine = create_engine("postgresql+psycopg2://postgres:1234@localhost:5432/orders")
metadata = MetaData()
# # объект поключения
# engine.connect()
# # установка соеденения с базой данных
# res = engine.connect().execute(text("SELECT * FROM public.users"))
# # получаем все записи из таблицы bd.student
# rows = res.fetchall()
# for row in rows:
#     print(row)
