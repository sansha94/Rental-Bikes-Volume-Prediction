import pandas as pd


def get_ftrs_from_date(
    df: pd.DataFrame
):
    # Preparing the datetime column
    df["datetime"] = df["Date"] + " " + df["Hour"].astype(str) + ":00"
    
    # Changing the data type to datetime
    df["datetime"] = pd.to_datetime(df["datetime"], format="%d/%m/%y %H:%M")
    
    # Casting Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%y")

    # Creating quarter column
    df["quarter"] = df["Year"].astype(str) + "0" + df["Date"].dt.quarter.astype(str)

    return df
