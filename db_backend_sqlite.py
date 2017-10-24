import sqlite3
"""
this script connects to local sqlite3 db.
"""

def create_table():
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, vin TEXT, auto TEXT, model TEXT, year INTEGER, name TEXT, surname TEXT, tel TEXT, email TEXT, data TEXT)")
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(vin="",auto="",model="",year="",name="",surname="",tel="",email="",data=""):
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM clients WHERE vin=? OR auto=? OR model=? OR year=? OR name=? OR surname=? OR tel=? OR email=? OR data=?", (vin,auto,model,year,name,surname,tel,email,data))
    rows = curr.fetchall()
    conn.close()
    return rows

def insert(vin,auto,model,year,name,surname,tel,email,data):
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO clients VALUES (NULL,?,?,?,?,?,?,?,?,?)",(vin,auto,model,year,name,surname,tel,email,data))
    conn.commit()
    conn.close()

def update(id,vin,auto,model,year,name,surname,tel,email,data):
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("UPDATE clients SET vin=?,auto=?,model=?,year=?,name=?,surname=?,tel=?,email=?,data=? WHERE id=?",(vin,auto,model,year,name,surname,tel,email,data,id))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("avtodelo.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM clients WHERE id=?",(id,))
    conn.commit()
    conn.close()

create_table()
