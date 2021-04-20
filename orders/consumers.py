from channels.generic.websocket import WebsocketConsumer
import json

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.account = self.scope['url_route']['kwargs']['account']
        self.send(json.dumps({"action": "subscribe", "account": self.account}))

    def disconnect(self, close_code):
        self.account = self.scope['url_route']['kwargs']['account']
        self.send(self.send(json.dumps({"action": "unsubscribe", "account": self.account})))


class WSConsumer1(WebsocketConsumer):
    def connect(self):
        self.accept()
        self.account = self.scope['url_route']['kwargs']['account']
        self.send(self.send(json.dumps({"action": "unsubscribe", "account": self.account})))