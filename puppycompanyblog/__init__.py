# puppycompanyblog/__init__.py

from flask import Flask

app = Flask(__name__)

from puppycompanyblog.core.views import core
from puppycompanyblog.error_pages.handler import error_pages

app.register_blueprint(core)
app.register_blueprint(error_pages)