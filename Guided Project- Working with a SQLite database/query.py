import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')

c = conn.cursor()
#type my sql query here
c.execute('SELECT name FROM facts ORDER BY population LIMIT 10;')
print(c.fetchall())
