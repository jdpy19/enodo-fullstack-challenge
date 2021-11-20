import os

DATA_DIR = os.environ.get('DATA_DIR')
DB_NAME = os.environ.get('DB')

class Config(object):
  DEBUG = True
  DEVELOPMENT = True
  TESTING = True

  CSRF_ENABLED = True
  SECRET_KEY = 'very-secret-key'
  API_PREFIX = 'api'
  
  # Database
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  USERNAME = 'postgres'
  PASSWORD = 'postgres'
  DATABASE = 'postgres'
  HOST = os.environ.get('HOST')
  PORT = 5432
  SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'

class ProductionConfig(Config):
  DEBUG = False
  DEVELOPMENT = False
  TESTING = False

CONFIGS = {
  'DEV': Config,
  'PRDO': ProductionConfig
}



