import random
import time
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, stock, price):
        pass


class StockMonitor:
    def __init__(self):
        self.observers = []
        self.stock_data = {"AAPL": 150.0, "GOOGL": 2800.0, "AMZN": 3500.0}

    def register_observer(self, observer:Observer):
        self.observers.append(observer)

    def unregister_observer(self, observer:Observer):
        self.observers.remove(observer)

    def notify_observers(self, stock, price):
        for observer in self.observers:
            observer.update(stock, price)

    def monitor_stock_prices(self):
        while True:
            for stock in self.stock_data:
                price_change = random.uniform(-5, 5)
                new_price = self.stock_data[stock] + price_change
                self.stock_data[stock] = new_price

                print(f"{stock} price updated: ${new_price:.2f}")
                self.notify_observers(stock, new_price)

            time.sleep(5)

    def get_stock_data(self):
        return self.stock_data

    def manual_update(self, stock, price):
        if stock in self.stock_data:
            self.stock_data[stock] = price
            print(f"Manual update: {stock} price set to ${price:.2f}")
            self.notify_observers(stock, price)
        else:
            print(f"Stock {stock} not found.")


if __name__ == "__main__":
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

    monitor.monitor_stock_prices()
