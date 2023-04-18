import pandas as pd
import json

def get_data(f):
    """
    This is a function that takes a file path and read in data
    with pandas
    : f: filepath
    : df: resulting data
    """
    if f.endswith('.csv'):
        df = pd.read_csv(f)
    elif f.endswith('.json'):
        json_data = open(f)
        df = json.load(json_data)
    elif f.endswith('.txt'):
        df = pd.read_csv(f, sep=",")
    else:
        print("Can only read in '.csv' or '.txt' or '.json' files")

    return df
