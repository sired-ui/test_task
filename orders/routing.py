from django.urls import path
from .consumers import WSConsumer, WSConsumer1

#wss://testnet.bitmex.com/realtime?subscribe=instrument,orderBookL2_25:XBTUSD
ws_urlpatterns = [
    path('ws/subscribe/<account>/', WSConsumer.as_asgi()),
    path('ws/unsubscribe/<account>/', WSConsumer1.as_asgi())
]