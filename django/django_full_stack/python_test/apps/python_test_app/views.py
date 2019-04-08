from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    if 'id' in request.session:
        return redirect('/success')
    else:
        return render(request, 'python_test_app/index.html')

def success(request):
    user_in_session = User.objects.get(id=request.session['id'])
    context = {
        'user': user_in_session
    }
    return render(request, 'python_test_app/wall.html', context)

def display(request):
    user = User.objects.get(id=request.session['id'])
    all_messages = Message.objects.all()
    all_comments = Comment.objects.all()
    context = {
        
        "all_messages": all_messages,
        "user": user,
    }
    return render(request,"python_test_app/wall.html", context)

def edit_account(request, id):
    if request.method == "POST":
        edit_response = User.objects.edit_validator(request.POST)
        if validation_response['valid']:
            new_user = validation_response['user']
            request.session['id'] = new_user.id
            edit = User.objects.get(id=id)
            edit.first_name = request.POST['fname']
            edit.last_name = request.POST['lname']
            edit.email = request.POST['email']
            edit.password = request.POST['password']
            edit.confirm_password = request.POST['confirm_password']
            edit.save()
            return redirect('/')
        else:
            user = User.objects.get(id=id)
            context = {
            "user" : user
            }
            return render (request,'python_test_app/edit_account.html',context)

def reg_user(request):
    if request.method == 'POST':
        validation_response = User.objects.reg_validator(request.POST)
        if validation_response['valid']:
            new_user = validation_response['user']
            request.session['id'] = new_user.id
            return redirect('/success')
        else:
            for error in validation_response['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def login(request):
    if request.method == 'POST':
        login_response = User.objects.log_validator(request.POST)
        if login_response['valid']:
            login_user = login_response['user']
            request.session['id'] = login_user.id
            return redirect('/success')
        else: 
            for error in login_response['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')

def add_quote(request):
    user = User.objects.get(id=request.session['id'])
    Message.objects.create(message = request.POST['quote'],user=author)
    return redirect('/')

def delete_message(request, id):
    message = Message.objects.get(id = id)
    message.delete()
    return redirect('/')

def add_comment(request):
    user = User.objects.get(id=request.session['id'])
    message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(comment = request.POST['comment'], user=user, message=message)
    return redirect('/')

def delete_comment(request, id):
    comment = Comment.objects.get(id = id)
    comment.delete()
    return redirect('/')
