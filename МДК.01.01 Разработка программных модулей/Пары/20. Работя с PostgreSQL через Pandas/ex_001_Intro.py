import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://postgres:123@localhost:5432/public')
# Строка подключения: СУБД+модуль://username:password@host:port/db_name
#==========================Чтение данных==========================#

query = "SELECT * FROM public.recipes"
df = pd.read_sql(query, engine)

print("Данные из таблицы recipes:")
print(df)
print(f'\nРазмерность DataFrame: {df.shape}')
print(f'Столбцы: {list(df.columns)}')
print(f'Типы данных:\n{df.dtypes}')
