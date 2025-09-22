from flask import Flask
from .config import Config
from .controllers.login_controller import login_blueprint
from .controllers.logout_controller import logout_blueprint
from .controllers.profile_info_controller import profile_info_blueprint
from .cors import init_cors
from .errors.handlers import init_error_handlers


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(logout_blueprint)
    app.register_blueprint(profile_info_blueprint)

    # Initialize database
    from app.database import init_db
    init_db()

    # Configure CORS
    init_cors(app)

    # Error handlers
    init_error_handlers(app)

    return app