import sqlite3
import pandas as pd

conn = sqlite3.connect('factbook.db')
c = conn.cursor()

c.execute('SELECT SUM(area_land) FROM facts WHERE area_land != "";')
d = c.fetchall()
area_land = d[0][0]

c.execute('SELECT SUM(area_water) FROM facts WHERE area_water != "";')
e = c.fetchall()
area_water = e[0][0]

print(area_land/float(area_water))