import pandas as pd
import os
from datetime import datetime

LOG_FILE = "analytics/chat_logs.csv"


def log_chat(question, mode, response_time):

    data = {
        "timestamp": [datetime.now()],
        "question": [question],
        "mode": [mode],
        "response_time": [response_time]
    }

    df = pd.DataFrame(data)

    if os.path.exists(LOG_FILE):

        old_df = pd.read_csv(LOG_FILE)

        df = pd.concat([old_df, df])

    df.to_csv(LOG_FILE, index=False)