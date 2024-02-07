import pandas as pd 
Name=['A','B','C','D','E']
Address=['Wardha','Nagpur','Mumbai','Nanded','Pune']
Salary=[5,4,3,8,9]

# df=pd.DataFrame(Name,Address,Salary)
# print(df)

data={"Name":Name,"Address":Address,"Salary": Salary}
df=pd.DataFrame(data)
print(df)

df.to_csv("abc.csv",index=False)