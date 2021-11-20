def create_models(db):
  models = {}
  for key, table in db.Model.metadata.tables.items():
    models[key] = type(key, (db.Model,), {
      '__table__': table
    })
  return models