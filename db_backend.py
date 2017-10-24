import psycopg2
"""
this script connects to romote DB on HEROKU.
"""

def create_table():
    conn = psycopg2.connect("dbname='database1' user='test_user' password='RolfBenz1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS avtodelo (id INTEGER PRIMARY KEY, vin TEXT, auto TEXT, model TEXT, year INTEGER, name TEXT, surname TEXT, tel INTEGER, email TEXT, data TEXT)")
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='database1' user='test_user' password='RolfBenz1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM avtodelo")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(vin="",auto="",model="",year="",name="",surname="",tel="",email="",data=""):
    conn = psycopg2.connect("dbname='database1' user='test_user' password='RolfBenz1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM avtodelo WHERE vin=%s auto=%s model=%s year=%s name=%s surname=%s tel=%s email=%s data=%s", (vin,auto,model,year,name,surname,tel,email,data))
    rows = curr.fetchall()
    conn.close()
    return rows

def insert(vin,auto,model,year,name,surname,tel,email,data):
    conn = psycopg2.connect("dbname='database1' user='test_user' password='RolfBenz1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO avtodelo VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(vin,auto,model,year,name,surname,tel,email,data))
    conn.commit()
    conn.close()

def update(id,vin,auto,model,year,name,surname,tel,email,data):
    conn = psycopg2.connect("dbname='database1' user='test_user' password='RolfBenz1' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE avtodelo SET vin=%s,auto=%s,model=%s,year=%s,name=%s,surname=%s,tel=%s,email=%s,data=%s WHERE id=%s",(vin,auto,model,year,name,surname,tel,email,data,id))
    conn.commit()
    conn.close()

create_table()
