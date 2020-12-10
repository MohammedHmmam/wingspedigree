from django.shortcuts import render

#Show All Pigeons
def pigeons_list(request):
    return render(request , 'pigeon/pigeons_list.html')