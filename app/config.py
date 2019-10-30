import os
from environs import Env


# get environment variables
env = Env()
env.read_env()


def create_config_object(env_setting):
    new_config = Config()
    with env.prefixed(env_setting):
        new_config.SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI")
        new_config.DEBUG = env.bool("DEBUG", default=False)
        new_config.TESTING = env.bool("TESTING", default=False)
    return new_config


class Config:
    """Set Flask configuration variables."""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = env.str(
        "SQLALCHEMY_DATABASE_URI", default=env.str("DEV_SQLALCHEMY_DATABASE_URI")
    )


DevelopmentConfig = create_config_object("DEV_")
# ProductionConfig = create_config_object("PROD_")
