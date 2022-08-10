#from crypt import methods
#from os import remove
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