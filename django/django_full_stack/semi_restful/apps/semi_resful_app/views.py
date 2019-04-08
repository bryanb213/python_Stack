from django.shortcuts import render, redirect
from . models import Show
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'shows':Show.objects.all()
    }
    return render(request, 'semi_restful_app/index.html', context)

def allshows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'semi_restful_app/all_shows.html', context)


def show_shows(request, id):
    show = Show.objects.get(id=id)
    context = {
        'shows': show
    }
    return render(request, 'semi_restful_app/show_shows.html', context)

def editshow(request, id):
    show = Show.objects.get(id=id)
    context = {
        'shows': show
    }
    return render(request, 'semi_restful_app/edit_show.html', context)

def addshow(request):
    if request.method == 'POST': 
        errors = Show.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/shows/new')
        else:
            show = Show.objects.create(title=request.POST['title'], network = request.POST['network'], desc=request.POST['desc'], date=request.POST['date'])
            return redirect('/shows/' + str(show.id))

def update(request, id):
    if request.method == 'POST':
        show = Show.objects.get(id=id)
        contexts = {
           'shows':show
        }
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.date = request.POST['date']
        show.desc = request.POST['desc']
        show.save()
    return redirect('/shows/' + str(show.id))

def delete(request, id):
    show = Show.objects.get(id=id)
    show.delete()
    return redirect('/shows')
