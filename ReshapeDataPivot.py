import pandas as pd


def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    print(weather.columns)

    return weather.pivot_table(values='temperature', index='month', columns='city', aggfunc='sum', fill_value=0)


data = [
    ["Jacksonville", "January", 13],
    ["Jacksonville", "February", 23],
    ["Jacksonville", "March", 38],
    ["Jacksonville", "April", 5],
    ["Jacksonville", "May", 34],
    ["ElPaso", "January", 20],
    ["ElPaso", "February", 6],
    ["ElPaso", "March", 26],
    ["ElPaso", "April", 2],
    ["ElPaso", "May", 43]
]

df = pd.DataFrame(data, columns=["city", "month", "temperature"])

pivot_df = pivotTable(df)

print(pivot_df)
