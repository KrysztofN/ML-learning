import pandas as pd

fruits = pd.DataFrame([["hello", "jessie"], [2,3]], columns=["a", "b"])


count = fruits.loc[0, 'a'].count('hello')
print(count)

a  =[1, 2, 3, 1]
print(a.count(1))