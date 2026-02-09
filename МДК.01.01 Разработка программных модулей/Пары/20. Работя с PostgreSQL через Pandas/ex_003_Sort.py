import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/public')

query = "SELECT * FROM public.recipes"
df = pd.read_sql(query, engine)

df_sort = df.sort_values(by="name") # Сортировка по названию
df_sort = df.sort_values(by="duration") # Сортировка по длительности

