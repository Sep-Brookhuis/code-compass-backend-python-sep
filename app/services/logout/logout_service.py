from flask import make_response, jsonify

class LogoutService:
    def __init__(self):
        pass

    def logout(self):
        response = make_response(jsonify({"ok": True, "message": "Logged out"}))
        response.delete_cookie(
            "jwt",
            httponly=True,
            secure=False,
            samesite="Lax",
        )
        return response

