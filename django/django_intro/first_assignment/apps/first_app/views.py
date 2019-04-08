from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("Placeholder to later display aa list of blogs")

def new(request):
    return HttpResponse('placeholder to dispay a new form to create a new blog')

def create(request):
    return redirect('/')

def show(request, num):
    return HttpResponse(f"placeholder to display blog number: {num}")

def edit(request, num):
    return HttpResponse(f"placeholder to edit blog number: {num}")

def destroy(request, num):
    return redirect("/")