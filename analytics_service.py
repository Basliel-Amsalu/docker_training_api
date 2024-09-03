from flask import Flask, request
from observer import Observer

class AnalyticsService(Observer):
    def update(self, event_type: str, data: dict):
        print(f"AnalyticsService: Analyzing event {event_type} with data {data}")
        return '', 204

app = Flask(__name__)
analytics_service = AnalyticsService()

@app.route('/update', methods=['POST'])
def update():
    event_payload = request.json
    analytics_service.update('OrderPlaced', event_payload)
    return '', 204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7003)
