import pandas as pd

def load_data(path = "C:/Users/steve/Desktop/Notebooks/Production-Code-Demo/rent_apartments.csv"):
    return pd.read_csv(path)

df = load_data()
print(df)