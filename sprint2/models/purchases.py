from sqlalchemy import MetaData, Column, Table, ForeignKey


metadata = MetaData()
purchases = Table("purchases", metadata,
    Column("user_id", ForeignKey("users.user_id")),
    Column("product_id", ForeignKey("products.product_id")),
)