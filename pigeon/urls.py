from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'pigeon'

urlpatterns = [
    url(r'^$' , views.pigeons_list , name='list'),
]