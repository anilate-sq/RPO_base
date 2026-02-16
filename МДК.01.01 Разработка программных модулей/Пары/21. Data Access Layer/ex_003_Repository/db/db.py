import pandas as pd
from sqlalchemy import create_engine

def get_conn():
    return create_engine('postgresql+psycopg2://postgres:123@localhost:5432/rpo_db')