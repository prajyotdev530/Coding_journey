from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name':'Patrick',
        'age':23,
        'Nationality':'US'

    }
    return render(request, 'index.html',context)
def counter(request):

    return render(request,'counter.html')