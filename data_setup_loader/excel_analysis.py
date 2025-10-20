import pandas as pd

# Excel file load
df = pd.read_excel("devops.xls")
df2 = pd.read_excel("Backend_Ai_dvelopment.xlsx")
merge = pd.concat([df,df2],ignore_index=True)

# print(df.columns.to_list())

print(merge.shape[0],df.shape[1])
print(merge.info())

# for i in df.columns:
#     print(df[i])