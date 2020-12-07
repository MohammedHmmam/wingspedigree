from django.shortcuts import render
from . models import Fancier

def fancier_list(request):
    fanciers = Fancier.objects.all().order_by('joinedDate')
    return render(request , 'fancier/fancier_list.html' , {'fanciers':fanciers})
