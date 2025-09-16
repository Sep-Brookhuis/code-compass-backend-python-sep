from flask import Flask, jsonify
from flask_cors import CORS
from .config import Config
from .controllers.login_controller import new_blueprint
from .errors import BadRequest, Unauthorized, Forbidden


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(new_blueprint)

    # Initialize database
    from app.database import init_db
    init_db()

    CORS(
        app,
        origins=app.config["FRONTEND_ORIGIN"],
        supports_credentials=True,
    )

    @app.errorhandler(BadRequest)
    def handle_bad_request(err):
        return jsonify({"ok": False, "error": str(err) or "Bad request"}), 400

    @app.errorhandler(Unauthorized)
    def handle_unauthorized(err):
        return jsonify({"ok": False, "error": str(err) or "Unauthorized"}), 401

    @app.errorhandler(Forbidden)
    def handle_forbidden(err):
        return jsonify({"ok": False, "error": str(err) or "Forbidden"}), 403

    return app