import sqlite3
from flask import Flask, url_for, redirect, session, render_template, request
from flask_bcrypt import Bcrypt
import random, string
from db_def import register_members_to_db, check_members
#import Password_Function

bcrypt = Bcrypt()

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

        hash_name = bcrypt.generate_password_hash(name)
        hash_password = bcrypt.generate_password_hash(password)

        register_members_to_db(hash_name, hash_password)
        return redirect(url_for("index"))

    else:
        return render_template("register.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        password = request.form["password"]

        hash_name = bcrypt.generate_password_hash(name)
        hash_password = bcrypt.generate_password_hash(password)

        #verify_hash_name = bcrypt.check_password_hash(hash_name, name )
        #verify_hash_password = bcrypt.check_password_hash(hash_password, password)

        if check_members(hash_name, hash_password):
            session["name"] = hash_name

        return redirect(url_for("home"))
    else:
        redirect(url_for("index"))

@app.route("/home", methods=["POST", "GET"])
def home():
    if "name" in session:
        return render_template("home.html", hash_name=session["name"])
    else:
        return "Name or Pasword is Incorrect"




@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))



if __name__ == "___main__":
    app.run(debug=True)