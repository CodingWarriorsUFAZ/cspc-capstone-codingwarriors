import pandas as pd

def test_dataset_columns():
    df = pd.read_csv("data/raw/battery_cycle_level_dataset_CLEAN_FINAL.csv")
    assert {"battery_id", "cycle", "capacity", "rul"} <= set(df.columns)
