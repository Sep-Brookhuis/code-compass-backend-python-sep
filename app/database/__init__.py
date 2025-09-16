from peewee import PostgresqlDatabase

import app
from app import all_models

db = PostgresqlDatabase(
    app.config["DB_NAME"],
    user=app.config["DB_USER"],
    password=app.config["DB_PASSWORD"],
    host=app.config["DB_HOST"],
    port=app.config["DB_PORT"],
    sslmode="require"
)

with db:
    db.create_tables(all_models)