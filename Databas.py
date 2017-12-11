import sqlite3

conn=sqlite3.connect('Maps.db')
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS Mapdata( Id INTEGER, Map TEXT )')

def data_entry(key, map):
    c.execute("INSERT INTO Mapdata (Id, Map) VALUES (?, ?) ",
              (key, map))
    conn.commit()

def close():
    if conn:
        conn.close()
        c.close()
def rowCount():
    c.execute("SELECT COUNT (*) FROM Mapdata")
    rowcount = c.fetchone()[0]
    return rowcount