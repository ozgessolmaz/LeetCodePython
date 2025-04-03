import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:


    return pd.concat([df1, df2], ignore_index=True)

data1 = [
    [1, "Mason", 8],
    [2, "Ava", 6],
    [3, "Taylor", 15],
    [4, "Georgia", 17]
]

data2 = [
    [5, "Leo", 7],
    [6, "Alex", 7]
]

df1 = pd.DataFrame(data1, columns=["student_id", "name", "age"])
df2 = pd.DataFrame(data2, columns=["student_id", "name", "age"])

df_combined = concatenateTables(df1, df2)

print(df_combined)
