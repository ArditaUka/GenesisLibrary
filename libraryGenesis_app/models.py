from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors={}
        if len(postData["first_name"])<2:
            errors["first_name"] = "First name must be at least 2 characters long"
        if len(postData["last_name"])<2:
            errors["last_name"] = "Last name must be at least 2 characters long"
        if len(postData["email"])<1:
            errors["email"] = "Email cannot be blank"
        if not EMAIL_REGEX.match(postData["email"]):
            errors["email"] = "Email is not valid"
        result = User.objects.filter(email=postData['email'])
        if len(result)>0:
            errors['email'] = "Email address is already registered"
        
        if len(postData["password"])<8:
            errors["password"] = "Password must be at least 8 characters long."
        elif postData["password"] != postData["confirm_password"]:
            errors["password"] = "Passwords do not match"
        return errors    

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
