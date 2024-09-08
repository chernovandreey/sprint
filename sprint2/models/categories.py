from sqlalchemy import Table, String, Integer, Column
from sprint2.konstring import metadata

categories = Table("categories", metadata,
Column("category_id", Integer(), primary_key=True),
    Column("departament", String(60), nullable=False),
)
