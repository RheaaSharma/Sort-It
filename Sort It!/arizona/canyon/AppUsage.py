import os
import datetime as dt


def redundant(filepath):
    redundant = []
    past_day = dt.date(dt.date.today().year + (dt.date.today().month - 6) // 12, abs(dt.date.today().month - 6), dt.date.today().day)
    
    directory = filepath
    for filename in os.scandir(directory):
        fileobj = os.stat(filename)
        accessTime = os.path.getmtime(filename)
        if dt.date.fromtimestamp(accessTime) < past_day and 'Windows' not in os.path.basename(filename) and 'desktop' not in os.path.basename(filename) and 'assembl' not in os.path.basename(filename) and 'Microsoft' not in os.path.basename(filename):
            redundant.append(os.path.basename(filename))
    
    return redundant
