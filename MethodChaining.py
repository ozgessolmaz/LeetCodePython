import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals.loc[animals['weight'] > 100].sort_values(by='weight', ascending=False)[['name']]



"""+----------+---------+-----+--------+
| name     | species | age | weight |
+----------+---------+-----+--------+
| Tatiana  | Snake   | 98  | 464    |
| Khaled   | Giraffe | 50  | 41     |
| Alex     | Leopard | 6   | 328    |
| Jonathan | Monkey  | 45  | 463    |
| Stefan   | Bear    | 100 | 50     |
| Tommy    | Panda   | 26  | 349    |
+----------+---------+-----+--------+

+----------+
| name     |
+----------+
| Tatiana  |
| Jonathan |
| Tommy    |
| Alex     |
+----------+
"""
data=[
    ["Tatiana", "Snake",98,464],
    ["Khaled", "Giraffe", 50, 41],
    ["Alex", "Leopard", 6, 328],
    ["Jonathan", "Monkey", 45, 463],
    ["Stefan", "Bear", 100, 50],
    ["Tommy", "Panda", 26, 349],

]


animals = pd.DataFrame(data, columns=["name", "species", "age", "weight"])

result = findHeavyAnimals(animals)

print(result)





