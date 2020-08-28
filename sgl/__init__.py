from flask import Flask

from sgl import logger
from sgl.converters import JsonEncoder
from sgl.plugins.google_maps import GOOGLE_MAPS


logger = logger


def create_app():
    app = Flask(__name__)
    app.config.from_object('sgl.settings.default')

    app.json_encoder = JsonEncoder

    GOOGLE_MAPS.init_app(app)

    _register_blueprints(app)

    return app


def _register_blueprints(app):
    from sgl.endpoints import BP as root

    app.register_blueprint(root)
