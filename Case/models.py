from datetime import datetime
from django.db import models


# Create your models here.
class OrderBookHistory(models.Model):
    maxFiled = models.FloatField(max_length=1000, blank=True)
    minFiled = models.FloatField(max_length=1000, blank=True)
    average = models.FloatField(max_length=1000, blank=True)
    total = models.FloatField(max_length=1000, blank=True)
    date = models.DateTimeField(default=datetime.now)


class OrderBookSellHistory(models.Model):
    maxFiled = models.FloatField(max_length=1000, blank=True)
    minFiled = models.FloatField(max_length=1000, blank=True)
    average = models.FloatField(max_length=1000, blank=True)
    total = models.FloatField(max_length=1000, blank=True)
    date = models.DateTimeField(default=datetime.now)
