from sprint2.konstring import metadata, engine
from sprint2.models import users, users_data, shops, shopping_cart, purchases, products, categories

#создание таблиц
metadata.create_all(engine)