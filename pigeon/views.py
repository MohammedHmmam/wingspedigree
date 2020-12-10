from django.shortcuts import render
from . models import Pigeon

#Show All Pigeons
def pigeons_list(request):
    pigeons = Pigeon.objects.all()
    return render(request , 'pigeon/pigeons_list.html', {'pigeons':pigeons})


#Show specific Pigeon detaisl in single page
def pigeon_details(request , slug):
    pigeon = Pigeon.objects.get(slug=slug)
    return render(request , 'pigeon/pigeon_details.html' , {'pigeon':pigeon})