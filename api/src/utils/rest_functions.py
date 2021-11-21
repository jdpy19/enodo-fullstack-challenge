def get_item(model, item_id):
  raise NotImplementedError

def put_item(session, model, item_id, data):
  item = model.query.get_or_404(item_id)
  for key, value in data.items():
    setattr(item, key, value)

  session.add(item)
  session.commit()
  return {'status_code': 200, 'message': 'success'}

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

  return {'status_code': 200, 'count': len(results), 'results': output_results}



