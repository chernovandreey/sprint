from sqlalchemy import Column, Table, ForeignKey
from sprint2.konstring import metadata


purchases = Table("purchases", metadata,
    Column("user_id", ForeignKey("users.user_id")),
    Column("product_id", ForeignKey("products.product_id")),
)