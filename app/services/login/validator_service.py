from flask import request
from app.errors.Unauthorized import Unauthorized
from app.errors.BadRequest import BadRequest

class Validator:
    def __init__(self):
        pass

    def validate_input(self):
        user_input = request.get_json(silent=True)

        if user_input is None:
            raise BadRequest("Request body must be JSON")

        email = user_input.get("email")
        password = user_input.get("password")

        if not email or not isinstance(email, str):
            raise Unauthorized("Invalid credentials")

        if not password or not isinstance(password, str):
            raise Unauthorized("Invalid credentials")

        if "@" not in email or "." not in email.split("@")[-1]:
            raise Unauthorized("Invalid email format")

        if len(password) < 8:
            raise Unauthorized("Password too short")


        return email,password