# KITE_AWS_DEMO

This is a demo Python project that:  
- Posts mock market data to Google Sheets  
- Uses a Google Service Account for Sheets API authentication  
- Is ready to be extended for real Kite API integration and AWS deployment

---

## Contents
- `post_to_sheets.py`: Module to post data to a Google Sheet  
- `test_post.py`: Example script to test posting functionality  
- `mock_kite_pipeline.py`: Generates mock market data for demonstration  
- `requirements.txt`: Python package dependencies  

---

## Setup
1. Create a Google Service Account and download `credentials.json`  
2. Share your Google Sheet with the service account email  
3. Set your Sheet ID in `post_to_sheets.py`  
4. Install dependencies:

```bash
pip install -r requirements.txt
Running

To run a simple demo:

python test_post.py


To run the mock pipeline continuously:

python mock_kite_pipeline.py

Notes

Do not commit credentials.json or any API keys

This is a mock pipeline; real Kite API integration requires client-provided credentials
