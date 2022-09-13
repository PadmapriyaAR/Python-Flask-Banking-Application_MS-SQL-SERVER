import sys
import csv
import os
from table import Base,bankuser
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.engine import URL
from flask import Flask
app = Flask(__name__)

connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-CP8GNGU\SQLEXPRESS01;DATABASE=Bank;Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)
Base.metadata.bind = engine
db = scoped_session(sessionmaker(bind=engine))



def userdata():

    id ='3'
    name ='Ami'
    password='python'
    address = '78 Mercury Street,VIC'
    email ='amibhagat@gmail.com' 
    phonenumber ='444563456' 
    accountno = '101'
    balance='5000'
    db.execute("SET IDENTITY_INSERT user_table ON")
    db.execute("INSERT INTO user_table (id,name,password,address,email,phonenumber,accountno,balance) VALUES (:i,:n,:ps,:a,:e,:ph,:ac,:ba)", {"i":id ,"n":name,"ps":password ,"a":address,"e":email,"ph":phonenumber,"ac":accountno,"ba":balance})
    db.commit()
    print("accounts Completed ............................................ ")



    id ='6'
    name ='Sri'
    password='python2'
    address = '86 Venus Streeet<NSW'
    email ='Srivalli@gmail.com' 
    phonenumber ='422829877' 
    accountno = '102'
    balance='100000'
    db.execute("INSERT INTO user_table (id,name,password,address,email,phonenumber,accountno,balance) VALUES (:i,:n,:ps,:a,:e,:ph,:ac,:ba)", {"i":id ,"n":name,"ps":password ,"a":address,"e":email,"ph":phonenumber,"ac":accountno,"ba":balance})
    db.commit()
    print("accounts Completed ............................................ ")

    
    id ='7'
    name ='padma'
    password='3python'
    address = '36 Earth Streeet,NSW'
    email ='padma@gmail.com' 
    phonenumber ='658982109' 
    accountno = '103'
    balance='7500'
    db.execute("INSERT INTO user_table (id,name,password,address,email,phonenumber,accountno,balance) VALUES (:i,:n,:ps,:a,:e,:ph,:ac,:ba)", {"i":id ,"n":name,"ps":password ,"a":address,"e":email,"ph":phonenumber,"ac":accountno,"ba":balance})
    db.commit()
    print("accounts Completed ............................................ ")
    
    id ='8'
    name ='Iresha'
    password='python4'
    address = '98 mars Street,NSW'
    email ='ires@gmail.com' 
    phonenumber ='467890484' 
    accountno = '104'
    balance='5740'
    db.execute("INSERT INTO user_table(id,name,password,address,email,phonenumber,accountno,balance) VALUES (:i,:n,:ps,:a,:e,:ph,:ac,:ba)", {"i":id ,"n":name,"ps":password ,"a":address,"e":email,"ph":phonenumber,"ac":accountno,"ba":balance})
    db.commit()
    print("accounts Completed ............................................ ")
    
    id ='9'
    name ='Marzia'
    password='python5'
    address = '99 pluto Street,Nsw'
    email ='marzsyeda@gmail.com' 
    phonenumber ='487992449' 
    accountno = '105'
    balance='9028'
    db.execute("INSERT INTO user_table (id,name,password,address,email,phonenumber,accountno,balance) VALUES (:i,:n,:ps,:a,:e,:ph,:ac,:ba)", {"i":id ,"n":name,"ps":password ,"a":address,"e":email,"ph":phonenumber,"ac":accountno,"ba":balance})
    db.commit()
    print("accounts Completed ............................................ ")
    
if __name__ == "__main__":
    userdata()