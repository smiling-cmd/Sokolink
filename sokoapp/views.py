from django.shortcuts import render, redirect
from sokoapp.models import *

# Create your views here.

def details(request):
    return render (request, 'portfolio-details.html')

def privacy(request):
    return render (request, 'privacy.html')

def starter(request):
    return render (request, 'starter-page.html')

def terms(request):
    return render (request, 'terms.html')

def services(request):
    return render (request, 'service-details.html')

def index(request):

    if request.method == 'Post':
        mycontact = contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            phone = request.POST['subject'],
            message = request.POST['message'],

        )
        mycontact.save()
        return redirect('/')
    else:
        return render(request, 'index,html')
    