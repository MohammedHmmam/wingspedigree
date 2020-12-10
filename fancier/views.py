from django.shortcuts import render,redirect
from . models import Fancier
from . import forms


#Create new Fancier
def new_fancier(request):
    if request.method == 'POST':
        form = forms.NewFancier(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fancier:list')
    else:
        form = forms.NewFancier()
    return render(request , 'fancier/new_fancier.html' , {'form':form})


#Show all fanciers
def fancier_list(request):
    fanciers = Fancier.objects.all().order_by('joinedDate')
    return render(request , 'fancier/fancier_list.html' , {'fanciers':fanciers})

#Show specific Fancier details
def fancier_details(request , slug):
    fancier = Fancier.objects.get(slug = slug)
    return render(request , 'fancier/fancier_details.html' , {'fancier':fancier})