from mickel.views import *
from django.urls import path

urlpatterns=[
    path('mickel/',hero,name='mickel'),
]