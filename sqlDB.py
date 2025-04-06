import datetime
import os
import sqlite3


def create_database(db_name="file_metadata.db"):
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

def display_all_entries(cursor):
    cursor.execute("SELECT * FROM files")
    rows = cursor.fetchall()
    print("\nAll entries in the database:")
    for row in rows:
        print(f"ID: {row[0]}, Filename: {row[1]}, Path: {row[2]}, Size: {row[3]},"
              f"Create Time: {row[4]}, Modified Time: {row[5]}, Hashcode: {row[6]}")

def insert_file(cursor, conn, Data):
    try:
        
        cursor.execute('''
            INSERT OR REPLACE INTO files (filename, file_path, file_size, create_time, modified_time, hashcode)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (Data[0], Data[1], Data[2], Data[3], Data[4], Data[5]))
        conn.commit()
        print(f"Inserted/Updated: {Data}")
    except Exception as e:
        print(f"Error inserting {Data}: {e}")
