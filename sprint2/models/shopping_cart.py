from sqlalchemy import MetaData, Table, String, Integer, Column

metadata = MetaData()
basket = Table("basket", metadata,
Column("id", Integer(), primary_key=True, auto_increment=True),
    Column("product", String(200), nullable=False),
    Column("price", Integer(), nullable=False),
    Column("user", String(50), nullable=False),
)
