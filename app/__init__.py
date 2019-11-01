# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


# globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    # create and configure the app
    flask_app = Flask(__name__, instance_relative_config=False)
    flask_app.config.from_object(Config)

    # initialize plugins
    db.init_app(flask_app)

    with flask_app.app_context():
        # import blueprint routes
        from .admin import routes as admin_routes
        from .users import routes as users_routes
        from .questions import routes as questions_routes
        from .comments import routes as comments_routes

        # register blueprints
        flask_app.register_blueprint(admin_routes.admin_bp)
        flask_app.register_blueprint(users_routes.users_bp)
        flask_app.register_blueprint(questions_routes.questions_bp)
        flask_app.register_blueprint(comments_routes.comments_bp)

        # create tables for our models
        db.create_all()

        return flask_app
