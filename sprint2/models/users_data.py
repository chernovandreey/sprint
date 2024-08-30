from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey


metadata = MetaData()
users_data = Table("users_date", metadata,
    Column("user_id", ForeignKey("users.user_id", primary_key=True)),
    Column("phone_number", Integer()),
    Column("password", String(16)),
)