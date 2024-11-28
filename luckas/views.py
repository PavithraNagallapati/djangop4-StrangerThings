from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def aboy(request):
    return HttpResponse('<h1>luckas is an angry boy in st</h1>')