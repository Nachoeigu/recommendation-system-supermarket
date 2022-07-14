import pandas as pd

def import_data():
    df = pd.read_csv('orders.csv')
    df.columns = df.columns.str.lower().map(lambda x : x.replace(' ','_'))

    return df

def convert_to_boolean(data):
    if data >= 1:
        return 1
    else:
        return 0
