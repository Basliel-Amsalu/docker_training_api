from flask import Flask, jsonify, request
from stock_monitor import StockMonitor

app = Flask(__name__)
monitor = StockMonitor()

from logging_service import LoggingService
from analytics_service import AnalyticsService
from notification_service import NotificationService

logging_service = LoggingService()
analytics_service = AnalyticsService()
notification_service = NotificationService()

monitor.register_observer(logging_service)
monitor.register_observer(analytics_service)
monitor.register_observer(notification_service)

@app.route('/stocks', methods=['GET'])
def get_stocks():
    return jsonify(monitor.get_stock_data())

@app.route('/stocks/<stock>', methods=['POST'])
def update_stock(stock):
    data = request.get_json()
    price = data.get('price')
    monitor.manual_update(stock, price)
    return jsonify({"message": f"{stock} price updated to ${price:.2f}"}), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
