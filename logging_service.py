import os
from stock_monitor import Observer


class LoggingService(Observer):
    def __init__(self):
        os.makedirs("/logs", exist_ok=True)

    def update(self, stock, price):
        with open("/logs/stock_prices.log", "a") as f:
            f.write(f"{stock} Stock Price: ${price:.2f}\n")
        print(f"Logged {stock} Stock Price: ${price:.2f}")


if __name__ == "__main__":
    print("Logging Service Running...")
