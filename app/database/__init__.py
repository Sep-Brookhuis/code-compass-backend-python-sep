from peewee import PostgresqlDatabase
from app.config import Config

db = PostgresqlDatabase(
    Config.DB_NAME,
    user=Config.DB_USER,
    password=Config.DB_PASSWORD,
    host=Config.DB_HOST,
    port=Config.DB_PORT,
    sslmode="require"
)

def init_db():
    from app.database.models import all_models
    with db:
        db.create_tables(all_models)