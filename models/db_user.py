from tortoise import fields
from tortoise.models import Model


class User(Model):
    user_id = fields.IntField(pk=True)
    token = fields.TextField(null=True)
    prefix = fields.TextField(default=".д")
    username = fields.TextField(default="Unknown")
    balance = fields.IntField(default=0)
    premium = fields.BooleanField(default=False)
    actions = fields.JSONField(default={"ignore": [], "trust": []})

    created_at = fields.DatetimeField(auto_now_add=True)
