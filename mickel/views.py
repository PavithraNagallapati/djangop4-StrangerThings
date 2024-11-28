from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hero(request):
    return HttpResponse('<h1>mickel is the hero of st</h1>')