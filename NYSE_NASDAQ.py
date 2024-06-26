# -*- coding: utf-8 -*-
"""Untitled36.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18jsGM6qQM8cfD9YNumZmwb5EWvcnWULr
"""

!pip install requests pandas openpyxl



import requests
import pandas as pd

# Function to download and process the NASDAQ listed companies
def get_nasdaq_companies():
    url = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&exchange=nasdaq&download=true"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "rows" in data["data"]:
            df = pd.DataFrame(data["data"]["rows"])
            return df
        else:
            print("No data found in the response.")
            return pd.DataFrame()
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return pd.DataFrame()

# Function to save the data to an Excel file
def save_to_excel(df, filename):
    df.to_excel(filename, index=False)

# Main function to execute the script
def main():
    nasdaq_companies = get_nasdaq_companies()

    if not nasdaq_companies.empty:
        save_to_excel(nasdaq_companies, "nasdaq_companies.xlsx")
        print("Data has been saved to nasdaq_companies.xlsx")
    else:
        print("No data to save.")

if __name__ == "__main__":
    main()