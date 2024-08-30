from sqlalchemy import MetaData, Table, String, Integer, Column, ForeignKey


metadata = MetaData()
products = Table("products", metadata,
Column("product_id", Integer(), primary_key=True),
    Column("product", String(60), nullable=False),
    Column("category", String(60), ForeignKey("categories.category_id")),
    Column("shop", String(60), ForeignKey("shops.shop_id")),
)