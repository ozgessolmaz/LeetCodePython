import numpy as np
import pandas as pd



def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students['name']=students['name'].replace("None", np.nan)
    return students.dropna(subset='name')


data=[
    [32,"Piper",5],
    [217,"None",19 ],
    [779,"Georgia",20],
    [849,"Willow",14]
]

df = pd.DataFrame(data, columns=['student_id','name','age'])

df = dropMissingData(df)

print(df)