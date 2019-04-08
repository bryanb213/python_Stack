from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.

def index(request):
    if 'user' in request.session:
        return redirect('/dashboard')
    return render(request, 'project_app/index.html')

def reg_user(request):
    if request.method == 'POST':
        valid_response = User.objects.reg_validator(request.POST)
        if valid_response['valid']:
            user = valid_response['user']
            request.session['id'] = user.id # set  session name(id) hold user info but only id
            return redirect('/yes')# redirect to url!!!!!
        else:
            print(valid_response['errors'])
            for error in valid_response['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
         
def login(request):
    if request.method == 'POST':
        valid_response = User.objects.login_validator(request.POST) #get post info
        print(valid_response)
        if valid_response['valid']:
            user = valid_response['user']#adding user by dictionay
            request.session['id'] = user.id # set  session name(id) hold user info but only id
            return redirect('/yes')
        else: 
            for error in valid_response['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')
        


def dashboard(request):
    user = User.objects.get(id=request.session['id']) #get user info by getting session
    context ={ 'user': user}
    return render(request, 'project_app/yes.html', context)

def add_message(request):
    if request.method == 'POST':
        user = User.objects.get(id=request.session['id'])
        
        print(request.POST)

        Quote.objects.create(quote=request.POST['quote'], author=request.POST['author'], post_user = user)
        print('------')
        return redirect('/show_message')

def show_message(request):
    print(request.session['id'])
    user = User.objects.get(id=request.session['id'])
    quotes = Quote.objects.all()
    print(Quote.objects.all().count())
    print(Quote.objects.first().quote)
    print('------')

   # all_quotes = Quote.objects.all()
    
    context = {
    #    'all_quotes' : all_quotes,
        'quotes': quotes,
        'user':user
    }
    return render(request, 'project_app/yes.html', context)

def logout(request):
    request.session.clear()
    return redirect('/')

def delete(request, id):
    delete = Quote.objects.get(id=id)
    delete.delete()
    return redirect('/show_message') 