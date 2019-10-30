# __init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
# import config


# globally accessible libraries
db = SQLAlchemy()

def create_app():
    """Construct the core application."""
    # create and configure the app
    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')
    app.config.from_object(Config)
    # app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://justinho:GRIDS@localhost:3306/inventory"
    # app.config["FLASK_APP"] = "main"
    # app.config["DEBUG"] = True
    # app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  

    # initialize plugins
    db.init_app(app)    

    with app.app_context():
        # include routes
        from . import routes        
        
        # create tables for our models
        db.create_all()



        @app.route('/')
        def hello():
            return 'Hello, World!'

        return app
