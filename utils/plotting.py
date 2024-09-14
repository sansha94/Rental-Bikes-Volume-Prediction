import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def show_hist(
    df: pd.DataFrame,
    x_axis: str,
    fig_size=(8, 5)
):
    plt.figure(figsize=fig_size)
    sns.histplot(x=x_axis, data=df)
    plt.show()


def show_heatmap(
    df: pd.DataFrame,
    nmrcl_cols: list,
    fig_size=(10, 6)
):
    plt.figure(figsize=fig_size)
    sns.heatmap(df[nmrcl_cols].corr(), annot=True)
    plt.show()


def show_time_series(
    df: pd.DataFrame,
    x_axis: str,
    y_axis: str,
    fig_size=(10, 6)
):
    plt.figure(figsize=fig_size)
    sns.lineplot(
        x=x_axis,
        y=y_axis,
        data=df
    )
    plt.show()


def show_boxplot(
    df: pd.DataFrame,
    x_axis: str,
    y_axis: str,
    fig_size=(10, 6)
):
    plt.figure(figsize=fig_size)
    sns.boxplot(
        x=x_axis,
        y=y_axis,
        data=df
    )
    plt.show()
