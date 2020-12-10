from django.shortcuts import render
from . models import Pigeon

#Show All Pigeons
def pigeons_list(request):
    pigeons = Pigeon.objects.all()
    return render(request , 'pigeon/pigeons_list.html', {'pigeons':pigeons})