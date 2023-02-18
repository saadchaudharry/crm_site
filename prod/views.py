from django.shortcuts import render,redirect
from .models import products

# Create your views here.


def main_view(request):
    prod = products.objects.filter().all()
    context ={'prod':prod}
    return render(request,"index.html",context)