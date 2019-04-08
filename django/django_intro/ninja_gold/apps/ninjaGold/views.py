from django.shortcuts import render, redirect, HttpResponse
import random, datetime
# Create your views here.
def home(request):
    if 'activity' not in request.session:
        request.session['activity'] = []
    if 'gold' not in  request.session:
        request.session['gold'] = 0
    return render(request, 'ninjaGold/index.html')

def process(request):
    if request.method == 'POST':
        if request.POST['building'] =='farm':
            money = random.randrange(10,21)
            request.session['gold'] += money
            request.session['activity'].insert(0,'<div class="green">Earned '+str(money)+ ' gold from '+ request.POST['building']+ '! '+ " (" +str(datetime.datetime.now())+")<br></div>")
        if request.POST['building'] =='cave':
            money = random.randrange(5,11)
            request.session['gold'] += money
            request.session['activity'].insert(0,'<div class="green">Earned '+str(money)+ ' gold from '+ request.POST['building']+ '! '+ " (" +str(datetime.datetime.now())+")<br></div>")
        if request.POST['building'] =='house':
            money = random.randrange(2,6)
            request.session['gold'] += money
            request.session['activity'].insert(0,'<div class="green">Earned '+str(money)+ ' gold from '+ request.POST['building']+ '! '+ " (" +str(datetime.datetime.now())+")<br></div>")
        if request.POST['building'] =='casino':
            money = random.randrange(-51,51)
            request.session['gold'] += money
            if money > 0:
                request.session['activity'].insert(0,'<div class="green">Earned '+str(money)+ ' gold from '+ request.POST['building']+ '! '+ " (" +str(datetime.datetime.now())+")<br></div>")
            else:
                request.session['activity'].insert(0,'<div class="red">Oh no you lost '+str(money)+ ' gold from '+ request.POST['building']+ '! '+ " (" +str(datetime.datetime.now())+")<br></div>")
        return redirect('/')

def clear(request):
    del request.session['gold']
    del request.session['activity']
    return redirect('/')