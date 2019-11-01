# admin/routes.py
from flask import Blueprint
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from .. import db


# set up a blueprint
admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route("/admin", methods=["GET"])
def admin():
    """Admin page route."""
    print("TODO")