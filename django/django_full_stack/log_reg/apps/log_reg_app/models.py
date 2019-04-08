# Create your models here.
from __future__ import unicode_literals
from django.db import models
import re, datetime

class Registration(models.Manager):
    def reg_validator(self, postData):
        errors = []
        if len(postData['fname']) < 1:
            errors.append("First name cannot be empty.")
        if len(postData['lname']) < 1:
            errors.append("Last name cannot be empty.")
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            errors.append("Invalid email format.")
        if len(postData['pw']) < 8:
            errors.append("Password must be 8 characters long.")
        if postData['pw'] != postData['cpw']:
            errors.append("The passwords you entered do not match.")
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

# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(Author, related_name="books")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

