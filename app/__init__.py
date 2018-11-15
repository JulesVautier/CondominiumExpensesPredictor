from .DataHelper import dataHelper
from flask import Flask
from flask_marshmallow import Marshmallow

flask_app = Flask(__name__)
flask_app.config['JSON_SORT_KEYS'] = False
ma = Marshmallow(flask_app)

import app.api