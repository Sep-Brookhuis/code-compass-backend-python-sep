from flask import Blueprint

from app.database.repositories.profile_repository import ProfileRepository
from app.services.login.login_service import LoginService

class LoginController:
    def __init__(self):
        self.login_service = LoginService()

    def route_login(self):
        return self.login_service.login()

    def test(self):
        profile_repository = ProfileRepository()
        return profile_repository.create_profile("rens", "admin")

controller = LoginController()
new_blueprint = Blueprint("blueprint", __name__, url_prefix="/api")
new_blueprint.add_url_rule("/test", "test", controller.route_login, methods=["POST"])
new_blueprint.add_url_rule("/login", "login", controller.route_login, methods=["POST"])