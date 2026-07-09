import pandas as pd
df=pd.read_csv('Project 3 - Police Data Udemy.csv')
df.dropna(how='all',inplace=True,axis='columns')
by_driver_gender=df.groupby('driver_gender').count()['violation'].sort_values(ascending=False)
searched_by_gender=df.groupby('driver_gender').count()['search_conducted']
df['stop_duration']=df.stop_duration.map(
    {"0-15 Min":7.5,
     "16-30 Min":23,
     "+30 Min":43
        }
    )
age_distribution_for_each_violation=df.groupby('violation').driver_age.describe()
print(age_distribution_for_each_violation)