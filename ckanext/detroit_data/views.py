from flask import Blueprint


detroit_data = Blueprint(
    "detroit_data", __name__)


def page():
    return "Hello, detroit_data!"


detroit_data.add_url_rule(
    "/detroit_data/page", view_func=page)


def get_blueprints():
    return [detroit_data]
