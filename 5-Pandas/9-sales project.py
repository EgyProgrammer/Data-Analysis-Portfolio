import pandas as pd
df=pd.read_excel('Sales-Data-Analysis.xlsx')
df.columns=df.loc[0]
df.columns.name = None
df.reset_index(drop=True,inplace=True)
df.drop(0,axis=0,inplace=True)
df.dropna(axis=1,inplace=True)
df["Manager"]=df['Manager'].str.replace(" +"," ",regex=True)
df['Date']=pd.to_datetime(df['Date'])
df=df.astype({'Price':'float64','Quantity':'float64','Order ID':'int64'})
most_prefered_payment_method=df['Payment Method'].value_counts().sort_values(ascending=False)
most_selling_products=df.groupby('Product')[['Quantity']].sum().sort_values('Quantity',ascending=False)
most_selling_products.reset_index(inplace=True)
df['Revenue']=round(df.Price*df.Quantity)
""" px.bar(most_selling_products,x='Product',y='Quantity',color='Product').show() """
most_proftitable_city=df.groupby('City')['Revenue'].sum(numeric_only=True).sort_values(ascending=False)
most_proftitable_manager=df.groupby('Manager')['Revenue'].sum().sort_values(ascending=False)
avg_nov_dec_revenue=df[
    (df.Date.dt.month==11)|
    (df.Date.dt.month==12)
    ]['Revenue'].aggregate('mean')
std_quantity_revenue=df[['Quantity','Revenue']].std()
""" px.line(df,x=df.Date.dt.month,y='Revenue').show() """
print(std_quantity_revenue)