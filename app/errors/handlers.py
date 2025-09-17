from flask import jsonify
from app.errors.BadRequest import BadRequest
from app.errors.NotFound import NotFound
from app.errors.Unauthorized import Unauthorized
from app.errors.Forbidden import Forbidden

def init_error_handlers(app):
    @app.errorhandler(BadRequest)
    def handle_bad_request(err):
        return jsonify({"ok": False, "error": str(err) or "Bad request"}), 400

    @app.errorhandler(Unauthorized)
    def handle_unauthorized(err):
        return jsonify({"ok": False, "error": str(err) or "Unauthorized"}), 401

    @app.errorhandler(Forbidden)
    def handle_forbidden(err):
        return jsonify({"ok": False, "error": str(err) or "Forbidden"}), 403

    @app.errorhandler(NotFound)
    def handle_not_found(err):
        return jsonify({"ok": False, "error": str(err) or "NotFound"}), 404