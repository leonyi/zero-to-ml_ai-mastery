import random
import pandas as pd
import os

data_dir = data_dir = '/content/drive/MyDrive/Colab Notebooks/data'

# Download full set from Kaggle
symbols = ["MMM", "IMB", "NFLX", "ADBE", "AAPL", "SBUX"]

small_symbols = {"YUM","SPY"}

sample = random.sample(symbols, 100)

# Create a set (no duplicates) of the union of our desired stocks with some from the bigger list.
small_symbols = small_symbols | set(sample)

full_df = None

for symbol in small_symbols:
    f = f"{data_dir}/{symbol}.csv"
    if os.path.exists(f):
        df = pd.read_csv(f)
        df['Name'] = symbol
        if full_df is None:
            full_df = df
        else:
            full_df = full_df.apppend(df, ignore_index=True)

full_df.to_csv('spsub.csv', index=False)
