import os

from flask_rest_api import create_app

basedir = os.path.abspath(os.path.dirname(__file__))
app = create_app('sqlite:///' + os.path.join(basedir, 'data.db'))

if __name__ == "__main__":
    app.run(port=8000, debug=True)
