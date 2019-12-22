"""Flask Web Application"""
__maintainer__ = 'Gary Frederick'
__license__ = 'MIT'
__version__ = '1.0.0'
# built-in Python Modules
import os
# external Python Modules
from flask import Flask, session, render_template, redirect

app = Flask(__name__)
host_url = None
port_num = 5000
flask_env = os.getenv('FLASK_ENV')
flask_debug = os.getenv('FLASK_DEBUG')

if flask_env == 'development':
    host_url = '127.0.0.1'
else:
    host_url = '0.0.0.0'


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return 'home'


if __name__ == "__main__":
    app.run(debug=True, host=host_url, port=port_num)
