from flask import Flask, request
import subprocess
import os

from flask.json import jsonify

from app import dataHelper

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    return 'hello world'


@app.route("/datas", methods=['GET'])
def getDatas():
    limit_one = request.args.get('limite_one', default=None, type=int)
    limit_two = request.args.get('limite_two', default=None, type=int)
    resp = dataHelper.getDatas(limit_one, limit_two)
    return jsonify(resp)


@app.route("/data/<int:id>", methods=['GET'])
def getData(id):
    resp = dataHelper.getData(id)
    return jsonify(resp)

@app.route("/data/<int:id>", methods=['DELETE'])
def deleteData(id):
    resp = dataHelper.deleteData(id)
    return jsonify(resp)

@app.route("/data", methods=['POST'])
def post_one_row():
    