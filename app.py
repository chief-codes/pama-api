import sqlite3
from flask import Flask, url_for, redirect, session, render_template, request
import random, string

def register_members_to_db(name,password):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO members(name, password) values(?,?)", (name,password))
        con.commit()
        con.close()

def check_members(name,password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("Select name, password FROM members WHERE name=? and password=?", (name,password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False

app = Flask(__name__)
app.secret_key = "wh1t_2_Do?"

#For password to be accepted it must meet the following requirements:
    #Not be less than 12 characters
    #Must contain at least 1 number
    #Must contain both lower and uppercase letters
    #Must contain special characters or punctuation

lower = string.ascii_lowercase # saves lowercase alphabets to lower
upper = string.ascii_uppercase # saves uppercase alphabets to upper
numbers = string.digits # saves numbers to numbers
punctuation = string.punctuation

def password_generator():
        all = lower + upper + numbers #+ characters.... combines lower, upper and numbers to form a list
        temp = random.sample(all, 12) # selects randomly 8 characters anf saves them as temp
        separator = ""
        password = separator.join(temp) 
        #print(password)

def password_validation(password):
    l,u,n,p = 0,0,0,0
    if len(password) >= 12:
        for char in password:
            if (char in lower):
                l+=1
                    
            if (char in upper):
                u+=1
                    
            if (char in numbers): 
                n+=1
                
            if (char in punctuation):
                p+=1
                
            if (l>=1 & u>=1 & n>=1 & p>=1):
                print("Password is VALID !!!!")
        
            elif l<1:
                print("Password must contain at least one lower case")
            elif u<1:
                print("Password must contain at least one upper case")
            elif n<1:
                print("Password must contain at least one number")
            elif p<1:
                print("Password must contain at least one punctuation")

            else:
                print("Password should be 12 or more characters!!!")
 

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        register_members_to_db(name,password)
        return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        if check_members(name,password):
            session["name"] = name

        return redirect(url_for("home"))
    else:
        redirect(url_for("index"))

@app.route("/home", methods=["POST", "GET"])
def home():
    if "name" in session:
        return render_template("home.html", name=session["name"])
    else:
        return "Name or Pasword is Incorrect"




@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "___main__":
    app.run(debug=True)