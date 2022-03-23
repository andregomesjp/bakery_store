"""Healthcheck controller class"""
import flask


class ControllerBase:
    def __init__(self, logger, blueprint_name, name):
        self._logger = logger
        self._blueprint_name = blueprint_name
        self._name = name


class HealthCheckController(ControllerBase):
    def __init__(self, logger):
        super().__init__(logger, "healthcheck_bp", "HealthCheckController")
        self._blueprint = flask.Blueprint(self._blueprint_name, self._name)
        self._blueprint.route("", methods=["GET"])(self.get)

    def get(self):
        """Performs a healthcheck on this server"""
        self._logger.info(f"Healtcheck")
        message = "not healthy"
        try:
            message = "healthy"
            resp = flask.jsonify(message)
            resp.status_code = 200
            return resp
        except Exception as e:
            message = e
            resp.status_code = 500
            return resp

    def get_blueprint(self):
        return self._blueprint