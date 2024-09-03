from stock_monitor import Observer


class NotificationService(Observer):
    def update(self, stock, price):
        if price > 3000:
            print(f"Notification: {stock} has reached a high price of ${price:.2f}!")
        elif price < 100:
            print(f"Notification: {stock} has dropped to a low price of ${price:.2f}!")


if __name__ == "__main__":
    print("Notification Service Running...")
