import sqlite3
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

def create_account_table():
    conn= sqlite3.connect("Registered_Accounts.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Registered_Passwords(Site_url TEXT, Username TEXT, Password STRING)")
    conn.commit()
    conn.close()

def create_table():
    conn= sqlite3.connect("database.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT members(name TEXT, password int)")
    conn.commit()
    conn.close()

def register_members_to_db(hash_name, hash_password):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO members(name, password) values(?,?)", (hash_name, hash_password))
        con.commit()
        con.close()

def check_members(hash_name, hash_password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("Select name, password FROM members WHERE name=? and password=?", (hash_name, hash_password))

    result = cur.fetchone()
    if result:
        return True
    else:
        return False

def register_accounts_to_db(Site_url, Username, Password):
    con = sqlite3.connect("Registered_Accounts.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Registered_Passwords(Site_url, Username, Password) values(?,?,?)", (Site_url, Username, Password))
    con.commit()
    con.close()

def delete():
    con =  sqlite3.connect("database.db")
    cur = con.cursor()
    cur.execute("DELETE FROM members")
    con.commit()
    con.close()

