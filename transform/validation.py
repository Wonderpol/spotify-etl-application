import pandas as pd
from datetime import datetime
import datetime


def check_if_valid_data(df: pd.DataFrame) -> bool:
    if df.empty:
        print("No songs. Execution finished")
        return False

    if pd.Series(df['played_at']).is_unique:
        pass
    else:
        raise ValueError("Primary key is duplicated")

    if df.isnull().values.any():
        raise ValueError("Found null value")

    # Check that all timestamps if song were played within 24h
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    timestamps = df["timestamp"].tolist()
    for timestamp in timestamps:
        if datetime.datetime.strptime(timestamp, '%Y-%m-%d') < yesterday:
            raise ValueError("At least one of the returned songs does not have a yesterday's timestamp")

    return True
