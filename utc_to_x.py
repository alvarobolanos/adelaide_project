from datetime import datetime
import time

def convert(utc):

    # Converting to local timezone
    now_timestamp = time.time()
    offset = (datetime.fromtimestamp(now_timestamp) - datetime.utcfromtimestamp(now_timestamp)).seconds
    delta = utc - offset
    converted_time = datetime.fromtimestamp(delta).strftime('%Y-%m-%d %H:%M:%S')
    return converted_time
