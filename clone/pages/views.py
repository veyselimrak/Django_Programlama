from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> INDEX SAYFASI </h1>")

# Create your views here.
