import random
import time
from post_to_sheets import post_data
from datetime import datetime

# List of instruments
symbols = ["NIFTY", "BANKNIFTY", "SENSEX"]

# Function to generate mock OHLC data
def generate_mock_data():
    data_rows = []
    for symbol in symbols:
        # Random closing price
        close_price = round(random.uniform(20000, 45000), 2)
        # Random open, high, low prices based on close
        open_price = round(close_price - random.uniform(10, 50), 2)
        high_price = round(close_price + random.uniform(10, 50), 2)
        low_price = round(close_price - random.uniform(20, 60), 2)
        volume = random.randint(1000, 5000)

        data_rows.append({
            "name": symbol,
            "price": close_price,
            "volume": volume,
            "open": open_price,
            "high": high_price,
            "low": low_price
        })
    return data_rows

# Run continuously
while True:
    data = generate_mock_data()
    
    # Prepare data for Google Sheets (timestamp + OHLC + volume)
    sheet_data = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for item in data:
        sheet_data.append([
            item["name"],
            item["open"],
            item["high"],
            item["low"],
            item["price"],  # closing price
            item["volume"]
        ])
    
    # Post to Google Sheet
    post_data(sheet_data)

    print(f"Posted {len(sheet_data)} rows at {timestamp}!")

    # Wait 10 seconds before next update
    time.sleep(10)


