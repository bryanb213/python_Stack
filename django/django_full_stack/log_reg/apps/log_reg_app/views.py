from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    if 'id' in request.session:
        return redirect('/success')
    else:
        return render(request, 'log_reg_app/index.html')

def success(request):
    user_in_session = User.objects.get(id=request.session['id'])
    context = {
        'user': user_in_session
    }
    return render(request, 'log_reg_app/yes.html', context)

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

def add_message(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['id'])
        context = {
        'user': user
        }

        return redirect('/')