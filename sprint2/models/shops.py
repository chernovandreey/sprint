from sqlalchemy import Table, String, Integer, Column, ForeignKey
from sprint2.konstring import metadata


shops = Table("shops", metadata,
Column("shop_id", Integer(), primary_key=True),
    Column("shop_name", String(60), nullable=False),
    Column("product", Integer(), ForeignKey("products.product_id")),
    Column("category", Integer(), ForeignKey("categories.category_id")),
)
