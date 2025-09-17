from flask_cors import CORS

def init_cors(app):
    CORS(
        app,
        origins=app.config["FRONTEND_ORIGIN"],
        supports_credentials=True,
    )