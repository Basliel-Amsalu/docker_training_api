from stock_monitor import Observer

class AnalyticsService(Observer):
    def update(self, stock, price):
        analysis = "High" if price > 2000 else "Normal"
        print(f"Analyzed {stock} Stock Price: ${price:.2f} - {analysis}")

if __name__ == "__main__":
    print("Analytics Service Running...")
