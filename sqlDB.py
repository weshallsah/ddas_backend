import datetime
import os
import sqlite3


def create_database(db_name="file_metadata.db"):
    global conn
    global cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS files (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            file_path TEXT UNIQUE,
            file_size INTEGER,
            create_time DATETIME,
            modified_time DATETIME,
            hashcode TEXT
        )
    ''')

    conn.commit()
    print(f"Database '{db_name}' and table 'files' created or connected successfully.")
    return conn, cursor

async def display_all_entries():
    print ("datas geting datat")
    cursor.execute("SELECT * FROM files")
    rows =  cursor.fetchall()
    return rows

def insert_file(Data):
    try:
            cursor.execute('''
                INSERT OR REPLACE INTO files (filename, file_path, file_size, create_time, modified_time, hashcode)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (Data[0], Data[1], Data[2], Data[3], Data[4], Data[5]))
            conn.commit()
            print(f"Inserted/Updated: {Data}")
    except Exception as e:
        print(f"Error inserting {Data}: {e}")

def search_file(Data):
    query = "SELECT id, hashcode FROM files WHERE 1=1"
    params = []

    query += " AND filename LIKE ?"
    params.append(f"%{Data[0]}%")

    query += " AND file_path LIKE ?"
    params.append(f"%{Data[1]}%")

    query += " AND create_time LIKE ?"
    params.append(f"%{Data[3]}%")

    cursor.execute(query, params)
    results = cursor.fetchall()

    if results:
        for row in results:
            if(row[1] == Data[5]):
                return True
        
    return False
