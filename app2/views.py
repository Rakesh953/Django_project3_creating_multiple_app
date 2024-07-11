from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2v1(request):
    return HttpResponse('<h1>app2 view1</h1>')
def app2v2(request):
    return HttpResponse('<h1>app2 view2</h1>')