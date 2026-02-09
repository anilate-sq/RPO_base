import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/public')

query = "SELECT * FROM public.recipes"
df = pd.read_sql(query, engine)

# По категории
soups = df[df["category_id"] == 1] # Получаю все супа
borsh = df[df["name"].str.contains("Борщ")] # Получаю все борщи
