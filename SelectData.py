import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['student_id'] == 101][['name', 'age']]

data = [
    [101, 'Ulysses', 13],
    [53, 'William', 10],
    [128, 'Henry', 6],
    [3, 'Henry', 11]
]

df = pd.DataFrame(data, columns=["student_id", "name", "age"])

result = selectData(df)
print(result)
