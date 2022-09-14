from flask import Flask,render_template,request,flash,flash
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.engine import URL
from sqlalchemy.orm import scoped_session, sessionmaker
from table import *
import csv
import os


app = Flask(__name__)
webimg = os.path.join("static")
app.config["UPLOAD"] = webimg

#database connection to Ms SQL Server
connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-CP8GNGU\SQLEXPRESS01;DATABASE=Bank;Trusted_Connection=yes"
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url)    
Base.metadata.bind = engine
Base.metadata.create_all(engine)
db = scoped_session(sessionmaker(bind=engine))
#homepage
@app.route("/")
def index():
    webimg1= os.path.join(app.config["UPLOAD"], "piggy.jpg")
    webimg2 = os.path.join(app.config["UPLOAD"], "why.jpg")
    return render_template("web.html",piggy=webimg1,why=webimg2)

# Saves details to the database
@app.route("/regdetails",methods=["POST","GET"])
def signup():
    if request.method == "POST":
        uid=request.form.get('uid')
        name = request.form.get('uname')
        mail = request.form.get('mail')
        address= request.form.get('address')
        phno = request.form.get('phone')
        query = user(user_id=uid,name=name,address=address,email=mail,phonenumber=phno)
        db.add(query)
        db.commit()
        
    return render_template("signup.html")


#validates username and password
@app.route('/login', methods=['POST', 'GET'] )
def signin():
        global data
        if request.method=="POST" and 'username' in request.form and 'password' in request.form:
            name = request.form.get("username")
            pswd = request.form.get("password")
            data=db.execute("Select *from user_table WHERE name =:n and password =:psd",{"n":name,"psd":pswd}).fetchone()
            for i in data:
                uid=data[0]
                name=data[1]
                address=data[3]
                email=data[4]
                phonenumber=data[5]
                acc=data[6]
                balance=data[7]
                
            return render_template('currentuserdetails.html',id=uid,uname=name,add=address,mail=email,no=phonenumber,acc=acc,bal=balance)
            
        else:
           flash(" Username or password not match.")
                
        return render_template("signin.html",signin=true)

#transfer amt from user to to user
@app.route("/transfer",methods=["POST","GET"])
def transfer():
    if request.method =='POST':
        fuser=request.form.get("fromuser")
        tuser=request.form.get("touser")
        amt=int(request.form.get("amount"))
        if fuser != tuser:
            fdata=db.execute("Select * from user_table where id=:i",{"i":fuser}).fetchone()
            tdata=db.execute("Select * from user_table where id=:i",{"i":tuser}).fetchone()
            if fdata is not None and tdata is not None:
                    from_balance=fdata.balance-amt
                    to_balance=tdata.balance+amt
                    db.execute("update user_table set balance = :b where id =:i",{"b":from_balance,"i":fuser})
                    db.commit()
                    db.execute("update user_table set balance = :b where id =:i",{"b":to_balance,"i":tuser})
                    db.commit()
            else:
                    flash(" NO amount to transfer")

    
    
    return render_template("transfer.html",id=id)


#Contact page saves request in a csv file
@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
          name = request.form.get('fname')
          lastname = request.form.get('lname')
          email=request.form.get('email')
          phno = request.form.get('phone')
          message=request.form.get('message')

          data=[name,lastname,email,phno,message]
          with open("user.csv",'a', newline='') as fo:
            csv_writer=csv.writer(fo)
            csv_writer.writerow(data[0:])
            fo.close()
    return render_template("contact.html")

#Signout will send us to home page.
@app.route("/signout",methods=["POST","GET"])
def signout():
    return render_template("web.html")


if __name__ == '__main__' :
    app.secret_key = os.urandom(12)
    app.run(debug=True)