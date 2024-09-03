import requests
from flask import Flask, request, jsonify
from observer import Observer

class EventManager:
    def __init__(self):
        self.observers = {}

    def register(self, event_type: str, observer: Observer):
        if event_type not in self.observers:
            self.observers[event_type] = []
        self.observers[event_type].append(observer)

    def unregister(self, event_type: str, observer: Observer):
        if event_type in self.observers:
            self.observers[event_type].remove(observer)

    def notify(self, event_type: str, data: dict):
        if event_type in self.observers:
            for observer in self.observers[event_type]:
                observer.update(event_type, data)


app = Flask(__name__)
event_manager = EventManager()

@app.route('/register', methods=['POST'])
def register_observer():
    observer_data = request.json
    event_type = observer_data['event_type']
    observer_url = observer_data['url']

    observer = RemoteObserver(observer_url)
    event_manager.register(event_type, observer)
    return jsonify({'message': f'Observer registered for {event_type}'})

@app.route('/unregister', methods=['POST'])
def unregister_observer():
    observer_data = request.json
    event_type = observer_data['event_type']
    observer_url = observer_data['url']

    observer = RemoteObserver(observer_url)
    event_manager.unregister(event_type, observer)
    return jsonify({'message': f'Observer unregistered from {event_type}'})

@app.route('/notify', methods=['POST'])
def notify_observers():
    event_data = request.json
    event_type = event_data['event_type']
    payload = event_data['payload']
    
    event_manager.notify(event_type, payload)
    return jsonify({'message': f'Observers notified for {event_type}'})

class RemoteObserver(Observer):
    def __init__(self, url):
        self.url = url

    def update(self, event_type: str, data: dict):
        requests.post(self.url, json=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000)
