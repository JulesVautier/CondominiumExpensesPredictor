from flask import Flask
import subprocess
import os

from app import dataHelper

app = Flask(__name__)


@app.route("/")
def HelloWorld():
    return 'hello world'


@app.route("/datas", methods=['GET'])
def getDatas():
    resp = dataHelper.getDataFrame()
    print(resp)
    return str(resp)


@app.route("/data/<int:id>", methods=['GET'])
def getData(id):
    resp = dataHelper.getData(id)
    print(resp)
    return str(resp)