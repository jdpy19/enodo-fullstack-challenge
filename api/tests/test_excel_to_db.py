from unittest import TestCase
import pandas as pd

from src.utils.excel_to_db import (
  clean_column_name,
  clean_dataframe,
  dataframe_to_table,
  create_tables
)


class TestExcelToDb(TestCase):
  def test_clean_column_name(self):
    column = 'Some column'
    self.assertEqual('SOME_COLUMN', clean_column_name(column))

  def test_clean_dataframe(self):
    df = pd.DataFrame.from_dict({
      'some column': [' hi ', '', ' test  '],
      'another column': [123, 1357, 0.4]
    })
    x = [
      {'SOME_COLUMN': 'hi', 'ANOTHER_COLUMN': 123.0, 'SELECTED': False}, 
      {'SOME_COLUMN': None, 'ANOTHER_COLUMN': 1357.0, 'SELECTED': False}, 
      {'SOME_COLUMN': 'test', 'ANOTHER_COLUMN': 0.4, 'SELECTED': False}
    ]
    self.assertEqual(x, clean_dataframe(df).to_dict(orient='records'))

  def test_dataframe_to_table(self):
    pass

  def test_create_tables(self):
    pass