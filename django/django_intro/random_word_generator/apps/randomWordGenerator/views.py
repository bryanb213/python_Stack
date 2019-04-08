from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request): 
    name = get_random_string(length=14)
    if request.method == 'POST':
        if 'number' in request.session:
            request.session['number'] += 1
        else:
            request.session['number'] = 1
            print(request.session['number'])
    print(name)
    context = {
        "name": name
    }
    print('getting stuff from this route')
    return render(request, 'randomWordGenerator/index.html', context)