import pandas as pd

csv_url = ("https://raw.githubusercontent.com/paiml/wineratings/main/wine-ratings.csv")
df = pd.read_csv(csv_url)
df.head()