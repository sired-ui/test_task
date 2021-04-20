from django.db import models


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=24)
    api_secret = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Order(models.Model):
    orderID = models.CharField(max_length=11)
    symbol = models.CharField(max_length=10)
    volume = models.CharField(max_length=15)
    timestamp = models.CharField(max_length=30)
    side = models.CharField(max_length=4)
    price = models.FloatField(max_length=15)
    account = models.ForeignKey('Account', related_name='orders', on_delete=models.CASCADE)

    def __str__(self):
        return self.symbol +' '+ self.orderID
