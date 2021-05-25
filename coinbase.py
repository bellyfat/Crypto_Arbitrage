import websocket, json

def initialize(ws):
    print("Coinbase socket has been opened")
    subscription_message = {
        'type': 'subscribe',
        'channels': [{
            'name': 'ticker',
            'product_ids': ['BTC-USD']
        }]
    }
    ws.send(json.dumps(subscription_message))

def on_message(ws, message):
    data = json.loads(message)
    print(data)
    

socket = 'wss://ws-feed.pro.coinbase.com'
ws = websocket.WebSocketApp(socket, on_open=initialize, on_message=on_message)
ws.run_forever()