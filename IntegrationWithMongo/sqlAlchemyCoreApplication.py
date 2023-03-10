from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData(schema='teste')
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(45), nullable=False),
    Column('email', String(60)),
    Column('nickname', String(50), nullable=False)

)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_db_obj = MetaData(schema='bank')
financial_infor = Table(
    'financial_info',
    metadata_db_obj,
    Column('ID', Integer, primary_key=True),
    Column()
)