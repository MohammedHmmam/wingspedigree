from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'fancier'

urlpatterns = [
    url(r'^$' , views.fancier_list , name="list"),
]