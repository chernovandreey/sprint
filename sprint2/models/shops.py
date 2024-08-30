from sqlalchemy import MetaData, Table, String, Integer, Column, ForeignKey

metadata = MetaData()
shops = Table("shops", metadata,
Column("shop_id", Integer(), primary_key=True),
    Column("shop_name", String(60), nullable=False),
    Column("product", String(60), ForeignKey("products.products_id")),
    Column("category", String(60), ForeignKey("categories.category_id")),
)
