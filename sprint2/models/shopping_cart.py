from sqlalchemy import Table, String, Integer, Column, ForeignKey
from sprint2.konstring import metadata


basket = Table("basket", metadata,
Column("basket_id", Integer(), primary_key=True, autoincrement=True),
    Column("product", String(200), nullable=False),
    Column("price", Integer(), nullable=False),
    Column("user", Integer(), ForeignKey("users.user_id")),
)
