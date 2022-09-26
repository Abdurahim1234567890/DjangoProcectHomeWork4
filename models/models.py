from django.db import models
from brands.models import *
# Create your models here.


class Model(models.Model):
    name = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    hp = models.IntegerField()
    nm = models.IntegerField()
    brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos', null=True)

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    def __str__(self):
        return self.name