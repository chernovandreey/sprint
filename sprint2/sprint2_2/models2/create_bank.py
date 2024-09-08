from sqlalchemy import Table, Integer, DECIMAL, Column
from sprint2.konstring import metadata


bank_accounts = Table("bank_accounts", metadata,
    Column("account_id", Integer()),
    Column("balance", DECIMAL(11,2)),
)