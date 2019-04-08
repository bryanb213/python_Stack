# Create your models here.
from __future__ import unicode_literals
from django.db import models
import re

class Validator(models.Manager):
    def reg_validator(self, postData):
        errors = []
        if len(postData['fname']) < 3:
            errors.append('fname must be longer than 3 characters')
        if len(postData['lname']) < 3:
            errors.append('lname must be longer than 3 characters')
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            errors.append("Invalid email format")
            
        # else:
        #     check_login_info = User.objects.filter(email=postData['email'])
        #     if len(check_login_info) > 0:
        #         errors.append('email already exist')#checks if email is alreadfy registered
        if len(postData['pw']) < 4:
            errors.append('must be longer than 3 characters')
        if postData['pw'] != postData['cpw']:
            errors.append('passswords need to match')

        # response = {
        #     'errors': errors, #hold errors
        #     'valid': True, # check if validations are correct
        #     'user': None #check user
        # }

        # if len(errors) > 0:
        #     response['valid'] = False #if no errors make user
        # else:
        #     user = User.objects.create(
        #         first_name=postData['fname'], 
        #         last_name=postData['lname'],
        #         email=postData['email'],
        #         password=postData['pw']
        #         )

        #     response['user'] = user# adding new user to user variable
        # return response
    
    def login_validator(self, postData):
        errors = [] 
        response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
        if not re.match(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$', postData['email']):
            errors.append("Invalid email format")
       #get user and check pw after you find the user
        login = User.objects.filter(email=postData['email'])
        if len(login)>0:   
            user = User.objects.get(email=postData['email'])
            if user.password == postData['pw']:
                response['user'] = user
            else:
                errors.append('Password does not match our records')
                response['valid'] =False
        else:
            errors.append('email does not exist')
      
        if len(errors) > 0:
            response['valid'] = False
            return response
        else:
            return response





class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=100)
    desc = models.TextField()
    objects = Validator()

class Quote (models.Model):
    author = models.TextField()
    quote = models.TextField()
    user = models.ForeignKey(User, related_name='quotes1')
    post_user = models.ForeignKey(User, related_name='quotes')
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)

