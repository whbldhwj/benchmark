import pandas as pd

df = pd.read_json('tb-output.json')
df.to_csv('tb-output.csv')