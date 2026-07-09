import pandas as pd
df=pd.read_csv(r'Project+1+-+Weather+Dataset.csv')
unique_wind_speed=df['Wind Speed_km/h'].unique()
weather=df[df.Weather=="Clear"]['Weather']
weather2=df.groupby('Weather').get_group('Clear')
speed=df[df['Wind Speed_km/h']==4]
nulls=df.isna().sum()
df.rename(columns={"Weather":"Weather Condition"},inplace=True)
mean_visibility=df['Visibility_km'].mean()
sdp=df['Press_kPa'].std()
var_rel_hum=df['Rel Hum_%'].var()
snow_occurence1=df[df['Weather Condition']=='Snow'].count()
snow_occurence2=df[df['Weather Condition'].str.contains("Snow")]
complex_query1=df[
    (df['Wind Speed_km/h']>24) &
    (df['Visibility_km']==25)
]
mean_for_each_weather_condition=df.groupby('Weather Condition').mean(numeric_only=True)
max_for_each_weather_condition=df.groupby('Weather Condition').max(numeric_only=True)
when_weather_is_fog=df[df['Weather Condition'].str.contains("Fog")]
clear_weather_or_visibility_more_40=df[
    (df['Weather Condition']=="Clear") |
    (df['Visibility_km']>40)
]
complex_query2=df[
    (df['Weather Condition']=="Clear") & 
    (df['Rel Hum_%']>50) |
    (df['Visibility_km']>40)
]
print(complex_query2)