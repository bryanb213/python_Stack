from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages 

def index(request):
    return render(request, 'App1/index.html')

def register(request):
    check = User.objects.regValidator(
        request.POST['first_name'],
        request.POST['last_name'],
        request.POST['email'],
        request.POST['password'],
        request.POST['password_confirm'],
        request.POST['dob'],
    )
    if not check ['valid']:
        for error in check['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/main')
    else:
        request.session['user_id'] = check['user'].id
        messages.add_message(request, messages.SUCCESS, 'Welcome!')
        return redirect('/quotes')

def login(request):
    check = User.objects.loginValidator(
        request.POST['email'],
        request.POST['password']
    )
    if not check ['valid']:
        for error in check['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/main')
    else:
        request.session['user_id'] = check['user'].id
        messages.add_message(request, messages.SUCCESS, 'Welcome!')
        return redirect('/quotes')

def logout(request):
    request.session.clear()
    return redirect('/main')

def quotes(request):
    user = User.objects.get(id=request.session['user_id'])
    all_quotes = Quote.objects.all()
    context={
        'all_quotes': all_quotes,
        'user': user,
    }
    return render(request, "app1/quotes.html", context)

def new_quote(request):
    user = User.objects.get(id=request.session['user_id'])
    Quote.objects.create(
    quoted_by= request.POST['quoted_by'],
    quote = request.POST['quote'],
    uploaded_by = user,
    )
    return redirect('/quotes')
    check = Quote.objects.PostValidator(
        request.POST['quoted_by'],
        request.POST['quote'],
    )
    if not check ['valid']:
        for error in check['errors']:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/quotes')
    else:
        request.session['quote_id'] = check['quote'].id
        messages.add_message(request, messages.SUCCESS, "welcome!")
        return redirect('/quotes')

def add_favorite(request, number):
    user = User.objects.get(id=request.session['user_id'])
    quote = Quote.objects.get(id= number)
    Favorite.objects.create(parent_quote=quote, added_by=user)
    return redirect('/quotes')

def delete(request, number):
    quote = Quote.objects.get(id=number)
    user.quotes.all()
    quote.delete()
    return redirect('/quotes')

def view_user(request, number):
    user = User.objects.get(id=number)
    context={
    'user': user,
    }
    return render(request, 'App1/viewuser.html', context)

def editpage(request, number):
    user = User.objects.get(id=number)
    context={
        'user': user,
    }
    return render(request, 'App1/editpage.html', context)

def edit_account(request, number):
    c = User.objects.get(id=number)
    c.first_name = request.POST['first_name']
    c.last_name = request.POST['last_name']
    c.email = request.POST['email']
    c.password = request.POST['password']
    c.password_confirm = request.POST['password_confirm']
    c.dob = request.POST['dob']
    c.save()
    return redirect('/quotes')