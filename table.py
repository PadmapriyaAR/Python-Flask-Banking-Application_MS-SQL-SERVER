from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy import DateTime


connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-CP8GNGU\SQLEXPRESS01;DATABASE=Bank;Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
Base = declarative_base()
#created a table userinfo to store the userdetails.
class user(Base):
    __tablename__='userinfo'
    user_id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False)
    address = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phonenumber = Column(Integer)


class bankuser(Base):
    __tablename__='user_table'
    id = Column(Integer,primary_key=True, autoincrement=True)
    name = Column(String(50),nullable=False)
    password=Column(String(50),nullable=False)
    address = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    phonenumber = Column(Integer)
    accountno = Column(Integer,unique=True)
    balance=Column(Integer,nullable=False)

    
# create tables
Base.metadata.create_all(engine)