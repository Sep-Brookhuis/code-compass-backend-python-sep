import jwt
import os
from flask import request


def read_jwt_role(jwt_key):
    # jwt_key = request.cookies.get("jwt")
    jwt_secret = os.getenv("JWT_SECRET")

    payload = jwt.decode(
        jwt_key,
        options={"verify_signature": False}
    )
    user_role = payload.get("app_metadata", {}).get("role")
    return user_role
