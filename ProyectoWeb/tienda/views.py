from django.shortcuts import render

# Create your views here.

def Tienda(request):

    return render(request,'tienda/tienda.html')