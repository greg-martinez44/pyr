import os
import pandas as pd
import pytest

from rfuncs import *

def test_read_csv_loads_dataframe():
    filename = os.path.join(os.path.dirname(__file__), "test_data", "Auto.csv")
    expected_df = pd.read_csv(filename)
    actual_df = read_csv(filename)

    pd.testing.assert_frame_equal(expected_df, actual_df)

def test_names_returns_dataframe_columns():
    filename = os.path.join(os.path.dirname(__file__), "test_data", "Auto.csv")
    expected_df = pd.read_csv(filename)
    expected_columns = expected_df.columns.tolist()
    actual_df = read_csv(filename)
    actual_columns = names(actual_df)

    assert set(expected_columns) == set(actual_columns)

