from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)


@app.route('/')
def root():
    return 'hello world!'


@app.route('/spec')
def spec():
    return jsonify(swagger(app))


import vmock
import v100