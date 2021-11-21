import os

from flask import Flask, jsonify, request

from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from .config import CONFIGS
from .utils.model_generator import create_models
from .utils.route_generator import create_routes
from .utils.excel_to_db import create_tables

PREFIX = os.environ.get('PREFIX', 'dev')

def create_app():
  app = Flask(__name__)
  env = os.environ.get('ENV', 'DEV')
  CORS(app)
  app.config.from_object(CONFIGS.get(env))
  return app
  
app = create_app()
db = SQLAlchemy(app)
create_tables(db.engine)
db.Model.metadata.reflect(db.engine)

models = create_models(db)

create_routes(app, db, 'properties', models.get('properties'), PREFIX)

@app.route(f'/')
def health_check():
  return jsonify({'message': 'success'})