from .DataHelper import dataHelper
from flask import Flask
from flask_marshmallow import Marshmallow

flask_app = Flask(__name__)
ma = Marshmallow(flask_app)

import app.api