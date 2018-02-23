from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager)
# Create your models here.
import json
from pymongo.write_concern import WriteConcern
from pymodm import MongoModel, fields

class User(MongoModel):
    first_name = fields.CharField(required=True)
    last_name = fields.CharField(required=True)
    password = fields.CharField(required=True)
    email = fields.CharField(required=True)
    user_id = fields.CharField(required=True)
    phone = fields.FloatField(required=False, default=1)

    def __str__(self):
        return self.email

    def get_name(self):
        return self.first_name + ' ' + self.last_name

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_phone(self):
        return self.phone

    class Meta(object):
        collection_name = 'Users'



