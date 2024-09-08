from sqlalchemy import Table, String, Integer, Column, ForeignKey
from sprint2.konstring import metadata


products = Table("products", metadata,
Column("product_id", Integer(), primary_key=True),
    Column("product", String(60), nullable=False),
    Column("category", Integer(), ForeignKey("categories.category_id")),
    Column("shop", Integer(), ForeignKey("shops.shop_id")),
    Column("price", Integer()),
           )