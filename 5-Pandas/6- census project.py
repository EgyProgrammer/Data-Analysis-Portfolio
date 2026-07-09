import pandas as pd
df=pd.read_csv('Census+2011.csv')
group_by_state=df.groupby("State_name")["Population"].sum(numeric_only=True)
based_on_religion=df.groupby("State_name")[["Muslims","Jains","Buddhists","Sikhs","Christians"]].sum(numeric_only=True)
male_workers_in_one_state1=df.groupby("State_name")["Male"].sum()["MAHARASHTRA"]
male_workers_in_one_state2=df[df["State_name"]=="MAHARASHTRA"]["Male_Workers"].sum()
pd.to_datetime()
print(male_workers_in_one_state2)