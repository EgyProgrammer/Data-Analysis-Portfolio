import pandas as pd
df=pd.read_csv('Salary_Dataset_DataScienceLovers.csv')
job_roles_avg_salary=df.groupby('Job Roles').mean(numeric_only=True)['Salary']
job_avg_salary_by_city=df.groupby('Location').mean(numeric_only=True)['Salary'].sort_values(ascending=False)
new_delhi_companies=df[
    (df.Location=='New Delhi') &
    (df.Rating==5)
    ].sort_values('Salary',ascending=False)
job_title_with_highest_salary_reported=df.groupby('Job Title')['Salary'].count().sort_values(ascending=False)
top_avg_salary_company_with_20_report=df[df['Salaries Reported']>=20].groupby('Company Name').mean(numeric_only=True).sort_values('Salary',ascending=False)
print(df)