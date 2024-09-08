from sprint2.konstring import metadata
from sqlalchemy import Table, Integer, DECIMAL, Column

orders = Table("orders", metadata,
    Column ("order_id", Integer()),
    Column ("customer_id", Integer()),
    Column ("total_amount", DECIMAL),
)