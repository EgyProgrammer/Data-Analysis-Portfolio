import pandas as pd
df=pd.read_csv("Project+2+-+Cars+Dataset.csv")
for i in df.columns:
    if df[i].dtypes=="str":
        continue
    else:
        meanvalue=df[i].mean(numeric_only=True)
        df.fillna({i:meanvalue},inplace=True)
make_types=df['Make'].value_counts()
origin_filter1=df[(df.Origin=="Asian") | (df.Origin=="Europe")]
origin_filter2=df[df['Origin'].isin({'Asian','Europe'})]
delete_rows_greater_than_4000=df[~(df['Weight']>4000)]
df['MPG_City']=df['MPG_City']+3
print(df['MPG_City'])