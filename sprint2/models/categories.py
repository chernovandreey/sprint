from sqlalchemy import MetaData, Table, String, Integer, Column


metadata = MetaData()
categories = Table("categories", metadata,
Column("category_id", Integer(), primary_key=True),
    Column("departament", String(60), nullable=False),
)
