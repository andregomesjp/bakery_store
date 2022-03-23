import flask
import bakery_service.common.config_loader as config_loader
import bakery_service.common.logger as logging
import bakery_service.controllers.healthcheck as hc


def create_app():
    config = config_loader.load_config()
    app = flask.Flask(__name__)
    logger = logging.create_logger(__name__, config)
    healthcheck_controller = hc.HealthCheckController(logger)
    app.register_blueprint(
        healthcheck_controller.get_blueprint(), url_prefix="/healthcheck"
    )
    return app
