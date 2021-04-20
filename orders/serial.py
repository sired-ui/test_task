from rest_framework import serializers

from .models import Order


class OrderSerializer(serializers.Serializer):
    orderID = serializers.CharField(max_length=120)
    symbol = serializers.CharField(max_length=10)
    volume = serializers.CharField(max_length=15)
    timestamp = serializers.CharField(max_length=30)
    side = serializers.CharField(max_length=4)
    price = serializers.FloatField()
    account_id = serializers.IntegerField()

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


class OrderDetSerializer(serializers.Serializer):
    orderID = serializers.CharField(max_length=120)
    symbol = serializers.CharField(max_length=10)
    volume = serializers.CharField(max_length=15)
    timestamp = serializers.TimeField()
    side = serializers.CharField(max_length=4)
    price = serializers.FloatField()
    account_id = serializers.IntegerField()


class NewOrderSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    volume = serializers.CharField(max_length=15)
    side = serializers.CharField(max_length=4)
    account_id = serializers.IntegerField()


class OrdersSerializer(serializers.Serializer):
    symbol = serializers.CharField(max_length=10)
    account_id = serializers.IntegerField()