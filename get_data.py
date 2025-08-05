# generate_data.py
import pandas as pd
import os

# Create synthetic dataset
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [25, 30, 35, 40, 28],
    "city": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
}

df = pd.DataFrame(data)

# Create directory
os.makedirs("data", exist_ok=True)

# Save as CSV
df.to_csv("data/raw_data.csv", index=False)
print("Raw data saved to data/raw_data.csv")
