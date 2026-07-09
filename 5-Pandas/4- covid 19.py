import pandas as pd
df=pd.read_csv(r"Covid_19_data.csv")
victumes_in_each_reagion=df.groupby('Region').sum(numeric_only=True)[['Confirmed','Deaths','Recovered']]
df=df[~(df.Confirmed<10)]
max_confirmed_region=df.groupby('Region').sum(numeric_only=True).sort_values(by='Confirmed',ascending=False)
min_deaths_region=df.groupby('Region').sum(numeric_only=True).sort_values(by='Deaths',ascending=True)
india_s_report=df[df.Region=="India"]
print(india_s_report)