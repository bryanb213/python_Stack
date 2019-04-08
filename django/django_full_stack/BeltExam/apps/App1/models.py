from django.db import models
import bcrypt

class UserManager(models.Manager):
    def regValidator(self, first_name, last_name, email, password, password_confirm, dob):
        errors = []
        if len(first_name) == 0:
            errors.append('the first name field cannot be blank')
        elif len(first_name) < 2:
            errors.append('the first name field must be at least 2 characters')
        elif first_name.isalpha() == False:
            errors.append('the first name field must contain only letters')
        if len(last_name) == 0:
            errors.append('the last name field cannot be blank')
        elif len(last_name) < 2:
            errors.append('the last name field must be at least 2 characters')
        elif last_name.isalpha() == False:
            errors.append('the last name field must contain only letters')
        if len(email) == 0:
            errors.append('please enter your email')
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingEmail) > 0:
                errors.append('email already in use')
        if len(password) == 0:
            errors.append('Please enter your password')
        elif len(password) < 8:
            errors.append('password must be at least 8 characters')
        if (password != password_confirm):
            errors.append('passwords do not match')
        if len(dob) == 0:
            errors.append('Please enter date of birth')
        
        Response= {
            "errors":errors,
            "valid":True,
            "user":None
        }
        if len(errors) > 0:

            Response['valid'] = False
            Response['errors'] = errors
        else:
            Response['user'] = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                email = email.lower(),
                password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()),
                dob = dob
            )
        return Response

    def loginValidator(self, email, password):
        errors=[]
        if len(email)<1:
            errors.append('Email is required!')
        else:
            usersMatchingEmail = User.objects.filter(email=email)
            if len(usersMatchingEmail)==0:
                errors.append('Unknown Email')
        if len(password) < 1:
            errors.append('password is required')
        elif len(password) < 8:
            errors.append('password Incorrect')
        
        Response = {
            'errors': errors,
            'valid': True,
            'user': None
        }
        if len(errors) == 0:
            if bcrypt.checkpw(password.encode(), usersMatchingEmail[0].password.encode()):
                Response['user'] = usersMatchingEmail[0]
            else:
                errors.append('Incorrect password!')
        if len(errors) > 0:
            Response['errors'] = errors
            Response['valid'] = False
        return Response

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    dob = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class QuoteManager(models.Manager):
    def PostValidator(self, quote, quoted_by):
        errors = []
        if len(quote) == 0:
            errors.append("Please provide quote field")
        if len(quoted_by) == 0:
            errors.append("Please provide quoted by field")
        
        Response ={
            'errors': errors,
            'valid': True,
            'quote': None
        }
        if len(errors) > 0:
            Response["valid"] = False,
            Response['errors'] = errors
        else:
            Response['quote'] = Quote.objects.create(
                  quoted_by = quoted_by,
                  quote = quote,
                  uploaded_by = request.session['user']
            )
        return Response

class Quote(models.Model):
    quoted_by = models.CharField(max_length=255)
    quote = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name="quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Favorite(models.Model):
    parent_quote = models.ForeignKey(Quote, related_name="favorites")
    added_by = models.ForeignKey(User, related_name="users")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
