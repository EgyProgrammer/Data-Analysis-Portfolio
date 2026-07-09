import pandas as pd
df=pd.read_csv("Housing+Data.csv")
df.date=pd.to_datetime(df.date)
df['Year']=df.date.dt.year
df.insert(1,"Month",df.date.dt.month) # insert column in selected position
df.drop(columns=['Year','Month'],inplace=True)
num_of_crimes=df[df['no_of_crimes']==0]
min_max_average_price=df['average_price'].groupby(df.date.dt.year).aggregate(['min','max'])
min_max_crime_per_area=df.groupby('area')['no_of_crimes'].aggregate(['min','max'])
count_average_area_price=df[df['average_price']<100000].area.value_counts()
print(count_average_area_price)