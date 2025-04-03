import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email', keep='first')


data=[
    [1,"Ella","emily@example.com"],
    [2,"David","michael@example.com"],
    [3,"Zachary","sarah@example.com"],
    [4,"Alice","john@example.com"],
    [5,"Finn","john@example.com"],
    [6,"Violet","alice@example.com"]
]

df = pd.DataFrame(data, columns=['customer_id', 'name', 'email'])

df = dropDuplicateEmails(df)

print(df)