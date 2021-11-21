from flask import request, jsonify
from .rest_functions import post_item, get_item, put_item, get_items, delete_item

from functools import wraps

def create_routes(app, db, route, model, prefix):
  def CreateFunction(func):
    func.__name__ += route
    @wraps(func)
    def decorated_function(*args, **kwargs):
      return func(*args, **kwargs)
    return decorated_function

  @app.route(f'/{prefix}/{route}', methods=['POST', 'GET'])
  @CreateFunction
  def handleItems():
    methods = {
      'GET': {
        'method': get_items,
        'kwargs': {
          'model': model,
          'filters': request.args.to_dict(),
        }
      },
      'POST': {
        'method': post_item,
        'kwargs': {
          'model': model,
          'data': request.get_json(),
        }
      },
    }
    
    method = methods.get(request.method).get('method')
    result = method(**methods.get(request.method).get('kwargs'))
    return result

  @app.route(f'/{prefix}/{route}/<item_id>', methods=['GET', 'PUT', 'DELETE'])
  @CreateFunction
  def handleItem(item_id):
    methods = {
      'GET': {
        'method': get_item,
        'kwargs': {
          'model': model,
          'item_id': item_id
        }
      },
      'PUT': {
        'method': put_item,
        'kwargs': {
          'model': model,
          'item_id': item_id,
          'data': request.get_json(),
          'session': db.session
        }
      },
      'DELETE': {
        'method': delete_item,
        'kwargs': {
          'model': model,
          'item_id': item_id
        }
      },
    }
    
    method = methods.get(request.method).get('method')
    result = method(**methods.get(request.method).get('kwargs'))
    return result