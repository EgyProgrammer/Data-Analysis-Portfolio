import pandas as pd
import seaborn as sb
from matplotlib.pyplot import show
df=pd.read_csv('ai_financial_market_daily_realistic_synthetic.csv')
df=df.astype({"Date":"datetime64[us]"})
df['Year']=df.Date.dt.year
amount_of_R_and_D=df.groupby('Company').sum(numeric_only=True)['R&D_Spending_USD_Mn'].reset_index()
""" sb.barplot(amount_of_R_and_D,x='Company',y='R&D_Spending_USD_Mn')
show() """
company_revenue=df.groupby('Company').sum(numeric_only=True)['AI_Revenue_USD_Mn']
open_ai_df,google_df,meta_df=df[df.Company=='OpenAI'],df[df.Company=='Google'],df[df.Company=='Meta']
max_stock=df.sort_values(by='Stock_Impact_%',ascending=False)[['Event','Stock_Impact_%']]
print(max_stock)