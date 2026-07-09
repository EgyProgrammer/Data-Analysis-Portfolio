import pandas as pd
df=pd.read_csv("Project+7+-+Udemy+Dataset.csv")
df["price"]=df["price"].replace("Free","0").astype('int64')
unique_subjects=df.subject.unique()
subjects_total_courses=df.subject.value_counts()
free_courses1=df[df["price"]==0]
free_courses2=df[df["is_paid"]==False]
paid_courses1=df[df["price"]!=0]
paid_courses2=df[df["is_paid"]==True]
top_selling=df.sort_values("num_subscribers",ascending=False)
least_selling=df.sort_values("num_subscribers",ascending=True)
cheap_graphic_design_courses=df[
    (df.subject=="Graphic Design") &
    (df.price<100)
]
python_realted_course=df[df['course_title'].str.contains("Python")]
""" _2015_courses=df[df['published_timestamp'].str.contains("2015")] """
df['published_timestamp']=pd.to_datetime(df['published_timestamp'])
_2015_courses=df[df['published_timestamp'].dt.year==2015]
max_subscriber_each_level1=df.groupby('level')['num_subscribers'].max(numeric_only=True)
max_subscriber_each_level2=df[df['num_subscribers'].isin(df.groupby('level')['num_subscribers'].max(numeric_only=True))]
print(max_subscriber_each_level2)