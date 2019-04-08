from django.shortcuts import render, HttpResponse, redirect
from . models import *
from django.contrib import messages


def index(request):
    if 'id' in request.session:
        return redirect('/wall')
    else:
        return render(request, 'wall_app/index.html')

def register(request):
    if request.method == 'POST':
        # validate form data
        print("///////////////////////////////")
        deervalid = User.objects.registerValidator(request.POST)
        # if valid:
        if deervalid['valid']:
            #   store user in session
            user = deervalid['user']
            request.session['id'] = user.id
            #   redirect to wall page
            return redirect('/wall')
            # else if invalid
            #   create error messages
            #   redirect to /
        else:
            for error in deervalid['errors']:
                messages.add_message(request, messages.ERROR, error)
            return redirect('/')

def display(request):
    user = User.objects.get(id=request.session['id'])
    all_messages = Message.objects.all()
    all_comments = Comment.objects.all()
    context = {
        
        "all_messages": all_messages,
        # "all_comments": all_comments,
        "user": user,
    }
    return render(request,"wall_app/wall.html", context)


def login(request):
    if request.method == 'POST':
        validation_response = User.objects.loginValidator(request.POST)
        if validation_response['valid']:
            user = validation_response['user']
            request.session['id'] = user.id
            return redirect('/wall')
        else:
            for error in validation_response['errors']:
                messages.add_message(request, messages.ERROR, error)
                return redirect('/')


def newMessage(request):
    user = User.objects.get(id=request.session['id'])
    Message.objects.create(message = request.POST['message'], user=user)
    return redirect('/wall')

def newComment(request):
    user = User.objects.get(id=request.session['id'])
    message = Message.objects.get(id=request.POST['message_id'])
    Comment.objects.create(comment = request.POST['comment'], user=user, message=message)
    return redirect('/wall')

def deleteComment(request, id):
    comment = Comment.objects.get(id = id)
    comment.delete()
    return redirect('/wall')

def deleteMessage(request, id):
    message = Message.objects.get(id = id)
    message.delete()
    return redirect('/wall')

def editMyAccount(request, id):
    if request.method == "POST":
        edit = User.objects.get(id=id)
        edit.first_name = request.POST['fname']
        edit.last_name = request.POST['lname']
        edit.email = request.POST['email']
        edit.password = request.POST['password']
        edit.confirm_password = request.POST['confirm_password']
        edit.save()
        return redirect('/wall')
    else:
        user = User.objects.get(id=id)
        context = {
            "user" : user
        }
        return render (request,'wall_app/edit_my_account.html',context)
    

def logout(request):
    request.session.clear()
    return redirect('/')    

