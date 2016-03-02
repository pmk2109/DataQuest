import pandas as pd
import sqlite3
import math

conn = sqlite3.connect('factbook.db')

df = pd.read_sql_query('SELECT * FROM facts', conn)
df_clean = df.dropna(axis=0)
df_clean = df_clean[df_clean['area_land']>0]

growth_rate = df_clean['population_growth']
init_pop = df_clean['population']

def compound_growth_rate(pop, rate):
    return pop*math.e**((rate/100)*35)
    
df_clean['pop2050'] = compound_growth_rate(init_pop, growth_rate)

df_clean_sort_pop2050 = df_clean.sort('pop2050', ascending=False)
print(df_clean_sort_pop2050[['name','population','pop2050']][:10])
