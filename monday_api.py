import os
import requests
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("MONDAY_API_KEY")

URL = "https://api.monday.com/v2"

HEADERS = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

DEALS_BOARD_ID = "5030219946"
WORKORDER_BOARD_ID = "5030219979"


# -----------------------------------------
# Clean Data
# -----------------------------------------

def clean_dataframe(df):

    # Replace empty strings with NA
    df = df.replace("", pd.NA)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces
    for col in df.columns:

        if df[col].dtype == "object":

            df[col] = df[col].astype(str).str.strip()

    return df


# -----------------------------------------
# Convert text numbers to numeric
# -----------------------------------------

def convert_numeric_columns(df):

    keywords = [
        "Amount",
        "Value",
        "Quantity",
        "Receivable",
        "Collected",
        "Probability",
        "Billed"
    ]

    for col in df.columns:

        if any(word.lower() in col.lower() for word in keywords):

            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", "", regex=False)
                .str.replace("₹", "", regex=False)
                .str.replace(" ", "", regex=False)
            )

            df[col] = pd.to_numeric(
                df[col],
                errors="coerce"
            )

    return df


# -----------------------------------------
# Read Board
# -----------------------------------------

def get_board_data(board_id):

    query = f"""
    {{
      boards(ids: {board_id}) {{
        items_page(limit: 500) {{
          items {{
            name
            column_values {{
              column {{
                title
              }}
              text
            }}
          }}
        }}
      }}
    }}
    """

    response = requests.post(
        URL,
        json={"query": query},
        headers=HEADERS
    )

    if response.status_code != 200:
        raise Exception("Unable to connect to Monday.com")

    data = response.json()

    if "errors" in data:
        raise Exception(data["errors"])

    items = data["data"]["boards"][0]["items_page"]["items"]

    rows = []

    for item in items:

        row = {}

        row["Item Name"] = item["name"]

        for col in item["column_values"]:

            row[col["column"]["title"]] = col["text"]

        rows.append(row)

    df = pd.DataFrame(rows)

    df = clean_dataframe(df)

    df = convert_numeric_columns(df)

    return df


# -----------------------------------------
# Deals
# -----------------------------------------

def get_deals():

    return get_board_data(DEALS_BOARD_ID)


# -----------------------------------------
# Work Orders
# -----------------------------------------

def get_workorders():

    return get_board_data(WORKORDER_BOARD_ID)