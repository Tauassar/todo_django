from django.shortcuts import render
from django.http import HttpResponse 


def homeView(request):
    return render(request, 'quickstart/home.html')


def aboutView(request):
    return render(request, 'quickstart/about.html')

def personnalView(request):
    return render(request, 'quickstart/personnal.html')