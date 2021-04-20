from django.urls import path
from .views import OrdersView, OrderView, Index

app_name = "Order"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('orders/', OrdersView.as_view()),
    path('orders/<str:pk>/',OrderView.as_view()),
    path('', Index.as_view())
    ]