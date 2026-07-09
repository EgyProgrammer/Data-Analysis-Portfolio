import pandas as pd
df=pd.read_csv(r'Netflix+Dataset.csv')
df=df.drop_duplicates()
null_values1=df[df.notnull()]
null_values2=df.isna().sum()
null_values2=df.isnull().sum()
extract_certain_movie=df.loc[df.Title=='House of Cards',['Show_Id','Director']]
""" df['Year']=pd.to_datetime(df['Release_Date']) """
df['Release_Date']=df['Release_Date'].astype('datetime64[ms]')
df['Year']=df['Release_Date'].dt.year
group_by_year=df.groupby('Year').count().sort_values('Show_Id',ascending=False)
movies_in_2020=df[(df.Year==2020) & (df.Category=='Movie')]
tv_shows_in_india=df[
    (df.Country=="India")&
    (df.Category=="TV Show")
]["Title"]
top_10_directors=df['Director'].value_counts().sort_values(ascending=False)
multiple_conditions=df[
    ((df.Category=="Movie") & (df.Type=="Comedies")) | (df.Country=="United Kingdom")
]
df=df.dropna()
tom_cruise=df[df.Cast.str.contains('Tom Cruise')]
ratings1=df['Rating'].unique()
ratings2=df['Rating'].nunique()
canadas_rating_14=df[
    (df.Country=="Canada")&
    (df.Rating=="TV-14")&
    (df.Category=="Movie")
].count().shape[0]
Rrated_TVSHOW_after_2018=df[
    (df['Category']=='TV Show')&
    (df['Rating']=="R")&
    (df['Year']>2018)
]
max_duration_movie=df['Duration'].max()
country_with_high_tv_shows=df.loc[df.Category=="TV Show"]["Country"].value_counts()
sort_by_year=df.sort_values('Year',ascending=False)
multiple_conditions2=df[
    ((df.Category=="Movie") & (df.Type=="Dramas")) |
    ((df.Category=="TV Show") & (df.Type=="Kids TV"))
]
print(multiple_conditions2)