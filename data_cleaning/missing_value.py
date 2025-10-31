#check status of missing value

#name = ['salman','sultan','unknown']
#quantity = [1,2,3,1,2,3,1,2,3,'not given']

import pandas as pd
import numpy as np
data = {'name':['salman','akib','humayun',None],'age':[25,np.nan,27,25],'city':['Dhaka','Khulna',None,'ctg']}

df  = pd.DataFrame(data)

print(df.isnull().sum())

#first identfy important column - features

# print(df.dropna(axis=1))

#task: 80% null thakle tokhni remove hobe

# df_filled_const = df.fillna({'name':'unknown','age':0,'city':'not given'})

# print(df_filled_const)

# df['age'].fillna(df['age'].mean(),inplace=True)

df['age'].fillna(df['age'].mode()[0],inplace=True)

print(df)

#task: forward fill, backward fill, interpolation: also know their usecase