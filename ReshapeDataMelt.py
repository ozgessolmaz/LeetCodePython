import pandas as pd


def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report, id_vars=["product"], var_name="quarter", value_name="sales")


data = [
    ['Umbrella', 417, 224, 379, 611],
    ['SleepingBag', 800, 936, 93, 875]
]

df = pd.DataFrame(data, columns=["product", "quarter_1", "quarter_2", "quarter_3", "quarter_4"])
print(df)
print("--------------")

reshaped_df = meltTable(df)
print(reshaped_df)
