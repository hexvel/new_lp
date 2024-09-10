from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    balance = fields.FloatField(default=0.0)
    token = fields.TextField(null=True)
    username = fields.TextField(default="Unknown")
    prefix = fields.TextField(default="ня")
    script_prefix = fields.TextField(default="ск")
    admin_prefix = fields.TextField(default="адм")


# class Script(Model):
#     user_id = fields.IntField(pk=True)
