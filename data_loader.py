import pandas as pd
import numpy as np


def load_data(path):

    df = pd.read_csv(path, dtype={"Instrument": "category"})

    df["datetime"] = pd.to_datetime(df["Date"] + " " + df["Time"])

    df = df.sort_values("datetime")

    price_df = df.pivot(index="datetime", columns="Instrument", values="Close")

    return price_df


def clean_data(price_df):

    price_df = price_df.ffill().bfill()

    z = (price_df - price_df.mean()) / price_df.std()

    price_df[z.abs() > 5] = np.nan

    price_df = price_df.ffill()

    return price_df
