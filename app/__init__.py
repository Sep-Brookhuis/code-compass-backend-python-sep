from flask import Flask
from .config import Config
from .controllers.login_controller import new_blueprint
from .cors import init_cors
from .errors.BadRequest import BadRequest
from .errors.Forbidden import Forbidden
from .errors.Unauthorized import Unauthorized
from .errors.handlers import init_error_handlers


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(new_blueprint)

    # Initialize database
    from app.database import init_db
    init_db()

    # Configure CORS
    init_cors(app)

    # Error handlers
    init_error_handlers(app)

    return app