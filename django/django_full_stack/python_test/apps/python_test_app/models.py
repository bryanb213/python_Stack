from __future__ import unicode_literals
from django.db import models
import re, datetime

class Registration(models.Manager):
    def reg_validator(self, postData):
        errors = []
        if len(postData['fname']) < 1:
            errors.append("First name is required.")
        if len(postData['lname']) < 1:
            errors.append("Last name is required.")
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            errors.append("Invalid email format.")
        if len(postData['pw']) < 8:
            errors.append("Password must be 8 characters long.")
        if postData['pw'] != postData['cpw']:
            errors.append("The passwords do not match.")
        response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
    
        if len(errors) > 0:
            response['valid'] = False
        else:
            new_user = User.objects.create(
            first_name = postData['fname'],
            last_name = postData['lname'],
            email = postData['email'],
            password = postData['pw'],
        )
            response['user'] = new_user
        return response

    def log_validator(self, postData):
        errors = []
        users = User.objects.filter(email=postData['email'])
        response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
        if users.count() > 0:
            this_user = User.objects.get(email=postData['email'])
            if postData['pw'] != this_user.password:
                errors.append("Password does not match our records.")
                response['valid'] = False
                return response
            else:
                response['user'] = this_user
                return response
        else:
            errors.append("Email does not exist.")
            response['valid'] = False
            return response
    def edit_validator(self, postData):
        errors = []
        if len(postData['fname']) < 1:
            errors.append("First name cannot be empty.")
        if len(postData['lname']) < 1:
            errors.append("Last name cannot be empty.")
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            errors.append("Invalid email format.")
        if len(postData['password']) < 8:
            errors.append("Password must be longer than 8 characters.")
        if postData['password'] != postData['confirm_password']:
            errors.append("Passwords do not match.")
        response =  {
            'errors': errors,
            'valid' : True,
            'user': None,
        }
        if len(errors) > 0:
            response['valid'] = False
        else:
            new_user = User.objects.create(
            first_name = postData['fname'],
            last_name = postData['lname'],
            email = postData['email'],
            password = postData['password'],
            )
            response['user'] = new_user
        return response
    def quote_validator(self, postData):
        errors = []
        if len(postData['author']) < 3:
            errors.append("Author's name must be longer than 3 characters.")
        if len(postData['quote']) < 10:
            errors.append("Quote must be longer than 10 characters.")
        response = {
            'errors' : errors,
            'valid' : True,
            'user' : None,
        }
        if len(errors) > 0:
            response['valid'] = False
        return response

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    objects = Registration()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments')
    message = models.ForeignKey(Message, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField
