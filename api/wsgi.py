
   
import os
from src.app import app

if __name__ == '__main__':
  env = os.environ.get('ENV')
  if env == 'PROD':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))
  else:
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT'))
  