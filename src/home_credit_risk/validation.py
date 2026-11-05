import pandas as pd

# tự kiểm tra không dùng dữ liệu khi nạp vào psql

def check_unique_key(df: pd.DataFrame, key: str) -> bool:
    return df[key].is_unique