def get_item(model, item_id):
  raise NotImplementedError

def put_item(model, item_id, data):
  raise NotImplementedError

def delete_item(model, item_id):
  raise NotImplementedError

def post_item(model, data):
  raise NotImplementedError

def get_items(model, filters):
  results = model.query.filter_by(**filters).all()
  item_columns = model.__table__.columns.keys()

  output_results = []
  for result in results:
    new_result = dict((key, getattr(result, key)) for key in item_columns)
    output_results.append(new_result)

  return {'count': len(results), 'results': output_results}



