# Monday.com Business Intelligence Agent

## Overview

This project is a Business Intelligence Agent built using Python and Streamlit.

It connects to Monday.com using the Monday.com API and answers business questions related to:

- Revenue
- Sales Pipeline
- Sector Performance
- Execution Status
- Billing Status
- Collection Status
- Leadership Summary
- Cross-board Analysis

## Technologies Used

- Python
- Streamlit
- Pandas
- Requests
- Monday.com GraphQL API
- python-dotenv

## Project Structure

```
app.py
agent.py
monday_api.py
utils.py
```

## Run

```bash
pip install -r requirements.txt

streamlit run app.py
```

## Features

- Live Monday.com integration
- Data cleaning
- Business insights
- Founder-level dashboard
