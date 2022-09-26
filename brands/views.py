from django.shortcuts import render
from .models import *
# Create your views here.


def brands(request):
    context = {
        'brands': Brand.objects.all()
    }
    return render(request, 'brands.html', context)