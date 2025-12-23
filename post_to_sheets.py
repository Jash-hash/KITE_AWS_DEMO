import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --------------------------
# Google Sheets API setup
# --------------------------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# --------------------------
# Open your sheet by ID
# --------------------------
SHEET_ID = ""
sheet = client.open_by_key(SHEET_ID).sheet1

# --------------------------
# Append header if empty
# --------------------------
if not sheet.get_all_values():
    sheet.append_row(["Timestamp", "Instrument", "Price", "Volume"])

# --------------------------
# Function to post data
# --------------------------
def post_data(data_rows):
    """
    data_rows: list of dicts with keys 'name', 'price', 'volume'
    """
    for item in data_rows:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet.append_row([timestamp, item['name'], item['price'], item['volume']])
    print(f"{len(data_rows)} rows posted at {timestamp}!")




