from django.shortcuts import render


def fancier_list(request):
    return render(request , 'fancier/fancier_list.html')
