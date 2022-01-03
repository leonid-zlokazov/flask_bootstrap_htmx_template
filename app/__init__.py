from flask import Flask

def create_app():
    app = Flask(__name__.split('.')[0])
    from .base import base
    app.register_blueprint(base.bp, url_prefix='/base')
    return app


