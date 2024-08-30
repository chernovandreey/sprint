from sqlalchemy import MetaData, Table, String, Integer, Column, DateTime, ForeignKey


metadata = MetaData()
users = Table("users", metadata,
    Column("user_id", Integer(), primary_key=True),
    Column("user", String(60), nullable=False),
    Column("registration", DateTime, nullable=False),
    Column("favorite_product", Integer(), ForeignKey("products.product_id")),
    Column("status", String(15)),
)
