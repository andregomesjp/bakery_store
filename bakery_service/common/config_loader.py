import os


class Config(object):
    """Parent configuration class."""

    DEBUG = False
    SECRET = os.getenv("APP_SECRET")
    DATABASE_URI = os.getenv("DATABASE_URI")
    NAME = "default"
    FORMAT = "%(asctime)s -- %(message)s"


class DevelopmentConfig(Config):
    """Configurations for Development."""

    DEBUG = True
    NAME = "dev"
    LEVEL = "INFO"


class ProductionConfig(Config):
    """Configurations for Production."""

    DEBUG = False
    TESTING = False
    NAME = "prod"
    LEVEL = "WARNING"


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}


def load_config():
    env = os.getenv("FLASK_ENV")
    if env is None:
        env = "development"
    return app_config[env]
