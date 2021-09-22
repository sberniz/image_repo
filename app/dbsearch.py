import sqlite3

def search(query):
    conn = sqlite3.connect('airplane_info.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
