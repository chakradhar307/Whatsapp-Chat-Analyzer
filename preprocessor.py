import re
import pandas as pd
from dateutil import parser

def preprocess(data):
    # Updated pattern to include optional AM/PM
    pattern = r'(\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?[AaPp][Mm])?)\s-\s'
    
    # Split messages and timestamps
    messages = re.split(pattern, data)[1:]  # Alternating: [date, message, date, message,...]
    
    dates = messages[::2]
    texts = messages[1::2]

    df = pd.DataFrame({'date_str': dates, 'user_message': texts})
    
    # Convert to datetime using parser (handles 12/24 hr formats)
    df['date'] = df['date_str'].apply(lambda x: parser.parse(x, dayfirst=True, fuzzy=True))

    # Split user and message
    users = []
    messages = []

    for message in df['user_message']:
        # Try splitting at first ": "
        entry = re.split(r'([\w\W]+?):\s', message, maxsplit=1)
        if len(entry) >= 3:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message', 'date_str'], inplace=True)

    # Extract date/time components
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Period (hour window)
    df['period'] = df['hour'].apply(lambda h: f"{h:02d}-{(h+1)%24:02d}" if h != 23 else "23-00")

    return df
