# admin/routes.py
from flask import Blueprint
from flask import current_app as app
# from .. import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# set up a blueprint
admin_bp = Blueprint('admin_bp', __name__)


@admin_bp.route("/admin", methods=["GET"])
def admin():
    """Admin page route."""
    print("TODO")