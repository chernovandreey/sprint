from sqlalchemy import Table, String, Integer, Column, DateTime, ForeignKey
from sprint2.konstring import metadata


users = Table("users", metadata,
    Column("user_id", Integer(), primary_key=True),
    Column("user", String(60), nullable=False),
    Column("registration", DateTime, nullable=False),
    Column("favorite_product", Integer(), ForeignKey("products.product_id")),
    Column("status", String(15)),
)
