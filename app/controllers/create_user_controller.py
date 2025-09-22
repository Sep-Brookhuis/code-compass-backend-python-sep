from app.services.create_user.create_user_service import CreateUserService
from flask import Blueprint

class CreateUserController:
    def __init__(self):
        self.create_user_service = CreateUserService()

    def route_create_user(self):
        return self.create_user_service.create_user()

controller = CreateUserController()
create_user_blueprint = Blueprint("create_user_blueprint", __name__, url_prefix="/api")
create_user_blueprint.add_url_rule("/create_user", "create_user", controller.route_create_user, methods=["POST"])