import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity']=products['quantity'].fillna(0)
    products['quantity']=products['quantity'].astype(int)
    return products

data=[
    ["Wristwatch",None,135],
    ["WirelessEarbuds", None,821],
    ["GolfClubs",779,9319],
    ["Printer",849,3051]
]

df=pd.DataFrame(data,columns=["name","quantity","price"])
df=fillMissingValues(df)
print(df)