from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    # return HttpResponse('Hello, World!')
    context = {'Name': 'Bobin'}
    return render(request, 'app1/home.html', context)

def about(request):
    context = {'Name': 'Bobin'}
    return render(request, 'app1/about.html', context)
