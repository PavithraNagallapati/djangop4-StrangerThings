from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def iboy(request):
    return HttpResponse('<h1>dustin is very intelligent and cute boy in st')