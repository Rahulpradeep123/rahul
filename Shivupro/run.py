from flask import Flask, render_template,request,session,url_for,redirect,flash
import sqlite3 as sql
import os
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy


UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/courseselection")
def courseselection():
    return render_template("courseselection.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/addmission")
def admission():
   return render_template("admission.html")

@app.route("/agbsc")
def agbsc():
    return render_template("agbsc.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/arts")
def arts():
    return render_template("arts.html")

@app.route("/collsec")
def collsec():
    return render_template("collsec.html")

@app.route("/commerce")
def commerce():
    return render_template("commerce.html")

@app.route("/degree")
def degree():
    return render_template("degree.html")

@app.route("/diplamo")
def diplamo():
    return render_template("diplamo.html")

@app.route("/engineering")
def engineering():
    return render_template("engineering.html")

@app.route("/admin_login")
def Subbu():
    return render_template("adminlogin.html")




@app.route("/mba")
def mba():
    return render_template("mba.html")

@app.route("/mca")
def mca():
    return render_template("mca.html")

@app.route("/mcom")
def mcom():
    return render_template("mcom.html")

@app.route("/medical")
def medical():
    return render_template("medical.html")

@app.route("/msc")
def msc():
    return render_template("msc.html")

@app.route("/science")
def science():
    return render_template("science.html")

@app.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")


@app.route("/adminreh")
def admin_login():
    return render_template("adminreh.html")

@app.route("/adminlogin")
def adminnlogin():
    return render_template("adminlogin.html")



@app.route("/regActionnn", methods = ["GET","POST"])
def regActi():
    msg=None
    if(request.method=="POST"):
        if (request.form["email"]!="" and  request.form["password"]!=""):
            email = request.form["email"]
            password = request.form["password"]
            
            with sql.connect("data.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  admin(email,password) VALUES('"+email+"','"+password+"')")
                msg = "Register Details submitted successfully"
                con.commit()
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("adminlogin.html", msg=msg)
    
    
             





@app.route("/admin_login_action", methods=['POST'])
def adminlog():
    msg = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        with sql.connect("data.db") as con:
            c = con.cursor()
            c.execute("SELECT email FROM admin WHERE email = ? AND password = ?", (email, password))
            admin = c.fetchall() 
            if admin:
                session["admin_logged_in"] = True
                session["admin_email"] = email
                flash("Admin login successful")
                return redirect(url_for('admin_dashboard'))
            else:
                msg = "Invalid credentials"
                flash("Admin login unsuccessful")
    return render_template("adminlogin.html", msg=msg)

@app.route("/admin_dashboard")
def admin_dashboard():
    if "admin_logged_in" not in session:
        return redirect(url_for('admin_login'))

    with sql.connect("data.db") as con:
        c = con.cursor()
        c.execute("SELECT username FROM registers")
        users = c.fetchall()
    return render_template("admin_dashboard.html", users=users)

@app.route("/delete_user", methods=['POST'])
def delete_user():
    if "admin_logged_in" not in session:
        return redirect(url_for('admin_login'))
    
    username = request.form['username']
    with sql.connect("data.db") as con:
        c = con.cursor()
        c.execute("DELETE FROM registers WHERE username = ?", (username,))
        con.commit()
        flash("User deleted successfully")
    return redirect(url_for('admin_dashboard'))

@app.route("/logout")
def logout():
    session.pop("admin_logged_in", None)
    session.pop("admin_email", None)  
    flash("Logged out successfully")
    return redirect(url_for('admin_login'))




       
@app.route("/regAction", methods = ["GET","POST"])
def regActio():
    msg=None
    if(request.method=="POST"):
        if (request.form["username"]!="" and request.form["email"]!=""and request.form["password"]!="" ):
            name = request.form["username"]
            email = request.form["email"]
            pasword = request.form["password"] 

            with sql.connect("data.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  registers(username,email,password) VALUES('"+name+"','"+email+"','"+pasword+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Someting went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("login.html", msg=msg)
        
           
@app.route("/loginAction",methods=['GET','POST'])
def loginAction():
    msg=None
    if (request.method == "POST"):
        username = request.form['username']
      
        password = request.form['password']
        
        with sql.connect("data.db") as con:
            c=con.cursor()
            c.execute("SELECT username,password  FROM registers WHERE username = '"+username+"' and password ='"+password+"'")
            r=c.fetchall()
            for i in r:
                if(username==i[0] and password==i[1]):
                    session["logedin"]=True
                    session["username"]=username
                    flash("LOGIN SUCCESSFULL")
                    return redirect("/courseselection")         
                else:
                    msg= "please enter valid username and password"
                    flash("LOGIN UNSUCCESSFULL")
            return render_template("login.html",msg=msg) 
        



@app.route("/details", methods = ["GET","POST"])
def detailsapp():
    msg=None
    if(request.method=="POST"):
        if (request.form["fullname"]!="" and request.form["email"]!="" and request.form["date"]!="" and request.form["nationality"]!="" and request.form["phone"]!=""and request.form["password"]!="" and request.form["Address"]!="" and request.form["gender"]!=""):
            fullname = request.form["fullname"]
            email = request.form["email"]
            date= request.form["date"] 
            nationality= request.form["nationality"]
            phone= request.form["phone"]
            password = request.form["password"] 
            Address= request.form["Address"]
            gender= request.form["gender"]
            
            with sql.connect("data.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  raja(fullname,email,date,nationality,phone,password,Address,gender) VALUES('"+fullname+"','"+email+"','"+date+"','"+nationality+"','"+phone+"','"+password+"','"+Address+"','"+gender+"')")
                msg = "Register Details submitted successfully"
                con.commit()
        
        else:
            msg="Something went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("success.html", msg=msg)

        

if __name__ == "__main__":
    app.run(debug=True)