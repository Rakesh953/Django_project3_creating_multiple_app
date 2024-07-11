from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app1v1(request):
    return HttpResponse('<h1>app1 view1</h1>')

def app1v2(request):
    return HttpResponse('<h1>app1 view2</h1>')