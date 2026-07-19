import csv

STOCK_PRICES = {"AAPL": 180, "TSLA": 250, "MSFT": 320, "GOOGL": 140, "AMZN": 145}
portfolio = []

print("Enter stock ticker and quantity (e.g. 'AAPL 10'). Press Enter with no input to finish.\n")

while True:
    entry = input("Stock and quantity: ").strip()
    if not entry:
        break

    parts = entry.split()
    if len(parts) != 2:
        print("Invalid format. Use: TICKER QUANTITY (e.g. AAPL 10)\n")
        continue

    ticker, qty_str = parts[0].upper(), parts[1]

    if ticker not in STOCK_PRICES:
        print(f"'{ticker}' not in price list. Available: {', '.join(STOCK_PRICES)}\n")
        continue

    try:
        qty = int(qty_str)
    except ValueError:
        print("Quantity must be a whole number.\n")
        continue

    if qty <= 0:
        print("Quantity must be positive.\n")
        continue

    portfolio.append((ticker, qty, STOCK_PRICES[ticker]))

if not portfolio:
    print("No stocks entered. Nothing to track.")
    exit()

total = 0
print("\n--- Portfolio Summary ---")
print(f"{'Ticker':<8} {'Qty':<6} {'Price':<8} {'Value':<8}")
print("-" * 32)
for ticker, qty, price in portfolio:
    value = qty * price
    total += value
    print(f"{ticker:<8} {qty:<6} ${price:<5} ${value:<5}")

print("-" * 32)
print(f"{'TOTAL':<16} ${total:<5}\n")

save = input("Save to file? (y/n): ").strip().lower()
if save == "y":
    filename = input("Filename (e.g. portfolio.csv or portfolio.txt): ").strip()
    if not filename:
        filename = "portfolio.csv"

    if filename.endswith(".csv"):
        with open(filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Ticker", "Quantity", "Price", "Value"])
            for ticker, qty, price in portfolio:
                writer.writerow([ticker, qty, price, qty * price])
            writer.writerow([])
            writer.writerow(["TOTAL", "", "", total])
    else:
        with open(filename, "w") as f:
            f.write("Portfolio Summary\n")
            f.write(f"{'Ticker':<8} {'Qty':<6} {'Price':<8} {'Value':<8}\n")
            f.write("-" * 32 + "\n")
            for ticker, qty, price in portfolio:
                f.write(f"{ticker:<8} {qty:<6} ${price:<5} ${qty * price:<5}\n")
            f.write("-" * 32 + "\n")
            f.write(f"{'TOTAL':<16} ${total:<5}\n")

    print(f"Saved to '{filename}'.")
