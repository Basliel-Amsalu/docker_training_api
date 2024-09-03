from flask import Flask, request
from observer import Observer

class LoggingService(Observer):
    def update(self, event_type: str, data: dict):
        log_message = f"LoggingService: Logging event {event_type} with data {data}\n"
        with open('/logs/events.log', 'a') as f:
            f.write(log_message)
        print(log_message)
        return '', 204

app = Flask(__name__)
logging_service = LoggingService()

@app.route('/update', methods=['POST'])
def update():
    event_payload = request.json
    logging_service.update('OrderPlaced', event_payload)
    return '', 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7002)
