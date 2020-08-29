import requests
import json
import pandas as pd

url = 'https://data.kcmo.org/resource/nrbe-p8am.json'

response = requests.get(url).json()

df = pd.DataFrame(response)

zipcodes = df.groupby('zip_code').count()
print(df.describe())
