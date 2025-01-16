from flask import Flask
import os.path

templates = os.path.join(os.getcwd(), 'templates')
static = os.path.join(os.getcwd(), 'static')
app = Flask(__name__, template_folder=templates, static_folder=static)

from app.backend import sorteio