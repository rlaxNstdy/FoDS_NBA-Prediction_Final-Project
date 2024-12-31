import pandas as pd

merged_df = pd.read_csv("all_nba_playerstats_2021-2025.csv")


missing_values = merged_df.isnull().sum()

print("Missing values per column:")
print(missing_values)

if missing_values.sum() > 0:
    print("\nThere are missing values in the dataset.")
else:
    print("\nThere are no missing values in the dataset.")
