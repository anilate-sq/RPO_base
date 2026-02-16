import pandas as pd
from sqlalchemy import create_engine

def get_conn():
    return create_engine('postgresql+psycopg2://postgres:EndryuConverse141719@localhost:5432/rpo_db')