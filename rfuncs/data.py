from typing import List
import pandas as pd

def read_csv(io: str, *args, **kwargs) -> pd.DataFrame:
    """Reads csv file and returns a dataframe."""
    return pd.read_csv(io, *args, **kwargs)

def names(df: pd.DataFrame) -> List[str]:
    """Returns a list of column names from df."""
    return df.columns.tolist()
