import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def show_hist(
    df: pd.DataFrame,
    x_axis: str
):
    plt.figure(figsize=(8, 5))
    sns.histplot(x=x_axis, data=df)
    plt.show()


def show_heatmap(
    df: pd.DataFrame,
    nmrcl_cols: list
):
    plt.figure(figsize=(10, 6))
    sns.heatmap(df[nmrcl_cols].corr(), annot=True)
    plt.show()


def show_time_series(
    df: pd.DataFrame,
    x_axis: str,
    y_axis: str
):
    plt.figure(figsize=(10, 6))
    sns.lineplot(
        x=x_axis,
        y=y_axis,
        data=df
    )
    plt.show()
