import pandas as pd

def process_data(uploaded_file):
    df = pd.read_csv(uploaded_file, encoding='ISO-8859-1')

    # Basic cleaning
    df.dropna(how='all', inplace=True)
    df.columns = [col.strip() for col in df.columns]
    return df
