import uuid
from peewee import UUIDField, CharField, DateTimeField, SQL
from app.database.models.base_model import BaseModel

class Profiles(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    display_name = CharField(max_length=255, null=True)
    role = CharField(max_length=64, null=True)
    email = CharField(max_length=255, null=True)

    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

