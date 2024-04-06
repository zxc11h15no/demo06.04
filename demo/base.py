import sqlite3
import os

base_path = "db.db"

def create_base():
    if(os.path.exists(base_path)):
        return
    connect = sqlite3.connect(base_path)
    cur = connect.cursor()

    sql_file = "./sql/sql.sql"
    with open(sql_file,"r") as file:
        script = file.read()
        cur.executescript(script)
        connect.commit()
        connect.close()

def insert_data(query,data):
    connect = sqlite3.connect(base_path)
    cur = connect.cursor()
    res = cur.execute(query,data).fetchone()
    connect.commit()
    connect.close()
    return res