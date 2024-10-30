import yfinance as yf

class Stock:
    def __init__(self, symbol, quantity, purchase_price):
        self.symbol = symbol.upper()
        self.quantity = quantity
        self.purchase_price = purchase_price

    def current_price(self):
        stock_data = yf.Ticker(self.symbol)
        current_price = stock_data.history(period="1d")["Close"].iloc[-1]
        return current_price

    def current_value(self):
        return self.quantity * self.current_price()

    def profit_loss(self):
        return (self.current_price() - self.purchase_price) * self.quantity

class Portfolio:
    def __init__(self):
        self.stocks = {}

    def add_stock(self, symbol, quantity, purchase_price):
        if symbol in self.stocks:
            print(f"Updating existing stock {symbol} in portfolio.")
            self.stocks[symbol].quantity += quantity
            self.stocks[symbol].purchase_price = purchase_price
        else:
            self.stocks[symbol] = Stock(symbol, quantity, purchase_price)
            print(f"Added {symbol} to portfolio.")

    def remove_stock(self, symbol):
        if symbol in self.stocks:
            del self.stocks[symbol]
            print(f"Removed {symbol} from portfolio.")
        else:
            print(f"Stock {symbol} not found in portfolio.")

    def view_portfolio(self):
        total_value = 0
        total_profit_loss = 0
        print("\nCurrent Portfolio:")
        print("Symbol\tQuantity\tPurchase Price\tCurrent Price\tCurrent Value\tProfit/Loss")
        for symbol, stock in self.stocks.items():
            current_price = stock.current_price()
            current_value = stock.current_value()
            profit_loss = stock.profit_loss()
            total_value += current_value
            total_profit_loss += profit_loss
            print(f"{symbol}\t{stock.quantity}\t\t{stock.purchase_price}\t\t{current_price:.2f}\t\t{current_value:.2f}\t\t{profit_loss:.2f}")
        
        print(f"\nTotal Portfolio Value: {total_value:.2f}")
        print(f"Total Profit/Loss: {total_profit_loss:.2f}\n")

# Example usage
portfolio = Portfolio()

# Adding stocks
portfolio.add_stock("AAPL", 10, 150.00)
portfolio.add_stock("GOOGL", 5, 2800.00)

# Viewing portfolio
portfolio.view_portfolio()

# Removing a stock
portfolio.remove_stock("AAPL")

# Viewing portfolio again
portfolio.view_portfolio()
