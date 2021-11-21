
import os
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.sql import text

DATA_DIR = os.environ.get('DATA_DIR')

def clean_column_name(column):
  column = column.replace(' ', '_')
  return column.upper()

def clean_dataframe(df):
  df.columns = map(clean_column_name, df.columns)
  df['SELECTED'] = False
  df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
  df = df.replace({
    '': None
  })
  df = df.apply(pd.to_numeric, errors='ignore')
  return df

def dataframe_to_table(df, engine, name):
  with engine.begin() as connection:
    df.to_sql(name, con=connection, if_exists='replace')
    stmt = f"ALTER TABLE {name} ADD PRIMARY KEY (index);"
    connection.execute(stmt)

def create_tables(engine):
  df = pd.read_excel(os.path.join(DATA_DIR, 'Enodo_Skills_Assessment_Data_File.xlsx'))
  df = clean_dataframe(df)
  dataframe_to_table(df, engine, 'properties')
