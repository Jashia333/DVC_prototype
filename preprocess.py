# preprocess.py
import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw_data.csv")

# New record to add
new_record = {"name": "David", "age": 40, "city": "Houston"}

# Append new record
df = pd.concat([df, pd.DataFrame([new_record])], ignore_index=True)

# Save it back (overwrite original file)
df.to_csv("data/raw_data.csv", index=False)

print("New record added to data/raw_data.csv")
