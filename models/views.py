from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def one_brand(request, id):
    if Model.objects.count() < id:
        return HttpResponse("error. PAGE NOT FOUND")
    context = {
        'models': Model.objects.all(),
        'brand': Brand.objects.get(id=id)
    }
    return render(request, 'one_brand.html', context)


def one_brand_model_series(request, brand_id, model_id):
    context = {
        'model': Model.objects.get(id=model_id),
        'series': Series.objects.filter(model_id=model_id)
    }
    return render(request, 'one_brand_model_series.html', context)