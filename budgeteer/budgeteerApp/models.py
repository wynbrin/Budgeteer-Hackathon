import datetime

from django.db import models
from django.utils import timezone
# Create your models here.
class Date(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)


class Info(models.Model):
    purchase_id = models.ForeignKey(Date, on_delete=models.CASCADE)
    income = models.IntegerField(default=0)
    expenses = models.IntegerField(default=0)
    description = models.CharField(max_length=500)
    reoccurring = models.BooleanField(default=0)
    essential = models.BooleanField(default=0)
    category =  models.CharField(max_length=500)
    date_entered = models.DateTimeField('date entered')
