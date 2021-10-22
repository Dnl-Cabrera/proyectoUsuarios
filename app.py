from flask import Flask
import os

app = Flask(__name__)

app.config['DEBUG'] = True

app.secret_key = os.urandom(24)

from apps import rutas_1
from apps import rutas_2
