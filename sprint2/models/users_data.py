from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sprint2.konstring import metadata


users_data = Table("users_data", metadata,
    Column("user_id", ForeignKey("users.user_id"), primary_key=True),
    Column("phone_number", Integer()),
    Column("password", String(16)),
)