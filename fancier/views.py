from django.shortcuts import render
from . models import Fancier
from . import forms


#Create new Fancier
def new_fancier(request):
    form = forms.NewFancier()
    return render(request , 'fancier/new_fancier.html' , {'form':form})

#Show all fanciers
def fancier_list(request):
    fanciers = Fancier.objects.all().order_by('joinedDate')
    return render(request , 'fancier/fancier_list.html' , {'fanciers':fanciers})
