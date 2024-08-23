import pandas as pd


def get_nmrcl_cols(
    df: pd.DataFrame
):
    nmrcl_cols = [col for col in df.columns if df[col].dtype not in ["object", "datetime64[ns]"]]
    
    return nmrcl_cols
