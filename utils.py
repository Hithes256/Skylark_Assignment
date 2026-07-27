import pandas as pd


def clean_dataframe(df):
    """
    Clean data coming from Monday.com
    """

    # Replace empty strings with NaN
    df = df.replace("", pd.NA)

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Remove extra spaces from text columns
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()

    return df


def convert_to_number(series):
    """
    Convert text values to numbers.
    Example:
    '12,500' -> 12500
    '₹15,000' -> 15000
    """

    return (
        pd.to_numeric(
            series.astype(str)
                  .str.replace(",", "", regex=False)
                  .str.replace("₹", "", regex=False),
            errors="coerce"
        )
        .fillna(0)
    )


def find_column(df, column_name):
    """
    Find a column without worrying about
    uppercase/lowercase.
    """

    for col in df.columns:
        if col.strip().lower() == column_name.strip().lower():
            return col

    return None