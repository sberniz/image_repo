import sqlite3

def search(query="SELECT * FROM airplane_info;"):
    if query == None or query == "":
        query = "SELECT * FROM airplane_info"
    conn = sqlite3.connect('airplane_info.sqlite3')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results
