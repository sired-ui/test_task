import json

from django.shortcuts import render

from .bitmex_api import new_order

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, Account
from .serial import OrderSerializer, OrderDetSerializer, NewOrderSerializer, OrdersSerializer


class OrdersView(APIView):
    def get(self, request):
        params = request.query_params
        acc_id = params.get('account',None)
        if acc_id!=None:
            orders = Order.objects.filter(account_id=acc_id)
            serializer = OrderSerializer(orders, many=True)
            return Response({"orders": serializer.data})
        else:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders,many=True)
            print(dict(serializer.data[0]))
            return Response({"orders": serializer.data})

    def post(self,request):
        order = request.data.get('order')
        serializer = NewOrderSerializer(data=order)
        data = request.data.get('article')
        if serializer.is_valid(raise_exception=True):
            account = Account.objects.get(id=serializer.data['account_id'])
            api_key, api_secret = account.api_key, account.api_secret
            symbol, side, orderQty = serializer.data['symbol'], serializer.data['side'], serializer.data['volume']
            order_new = new_order(symbol, side, orderQty, api_key, api_secret)
            print('Result')
            order_new = json.loads(order_new)
            print(order_new)
            print(order_new['orderID'])
            order = {"orderID":order_new['orderID'],
                     "symbol":order_new['symbol'],
                     "volume":str(order_new['orderQty']),
                     "timestamp":order_new['timestamp'],
                     "side":order_new['side'],
                     "price":str(order_new['price']),
                     "account_id":serializer.data['account_id']}
            serializer = OrderSerializer(data=order)
            if serializer.is_valid(raise_exception=True):
                order_saved = serializer.save()
        return Response({"success":"Order '{}' created successfully".format(order_saved.orderID)})


class OrderView(APIView):
    def get(self, request, pk):
        order = Order.objects.get(orderID=pk)
        serializer = OrderDetSerializer(order)
        return Response(serializer.data)


class Index(APIView):
    def get(self, request):
        print(request.GET.get('account'))
        account = request.GET.get('account')
        return render(request, "index.html",context={"text":account})