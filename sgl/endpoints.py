from flask import (
    Blueprint,
    render_template,
    current_app,
    request,
)
from flask_googlemaps import Map

from sgl import crawler
from sgl import utils
from sgl.forms import QueryForm


BP = Blueprint('root', __name__)


@BP.route("/", methods=["GET"])
def index():
    form = QueryForm()

    return render_template(
        'index.html',
        title=current_app.config.get('PAGE_TITLE'),
        form=form,
    )


@BP.route("/map", methods=["POST"])
def query_map():
    payload = request.json or request.form
    payload = payload.to_dict(flat=False)
    print(payload)

    houses = crawler.get_houses(payload)

    markers = utils.get_markers(houses)

    lat, lng = utils.get_center_spot(houses)

    google_map = Map(
        identifier='sgl_map',
        lat=lat,
        lng=lng,
        markers=markers,
        style='height:80%;width:80%;margin:1%;',
        language='zh-tw',
        region='TW',
    )

    # TODO: Show house images
    return render_template(
        'map.html',
        title=current_app.config.get('PAGE_TITLE'),
        google_map=google_map,
    )
