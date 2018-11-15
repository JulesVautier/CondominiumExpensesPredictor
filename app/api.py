from flask import Flask, request
import subprocess
import os

from app import dataHelper

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    return 'hello world'


@app.route("/datas", methods=['GET'])
def getDatas():
    limite_one = request.args.get('limite_one', default=None, type=int)
    limite_two = request.args.get('limite_two', default=None, type=int)
    resp = dataHelper.getDatas(limite_one, limite_two)
    return str(resp)


@app.route("/data/<int:id>", methods=['GET'])
def getData(id):
    resp = dataHelper.getData(id)
    return str(resp)
