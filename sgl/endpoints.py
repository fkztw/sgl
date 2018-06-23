from flask import Blueprint, Response

BP = Blueprint('root', __name__)


@BP.route("/", methods=["GET"])
def index():
    return Response()
