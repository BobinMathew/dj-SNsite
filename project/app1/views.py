from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse('Hello, World!')
    context = {'Name': 'Bobin'}
    return render(request, 'app1/index.html', context)
