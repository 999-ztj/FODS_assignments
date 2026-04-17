"""
This program reads health_data.csv into a Pandas DataFrame and adds
two new columns: BMI (Weight / Height) and Health_Status based on
the BMI value ranges provided.
"""

import pandas as pd

# Read the CSV file
df = pd.read_csv("health_data.csv")

print("Original data (first 5 rows):")
print(df.head())
print()

# BMI is typically calculated as weight / (height^2),
# but assignment specifies weight / height, so we follow that.
df["BMI"] = df["weight"] / df["height"]

# Round BMI to 2 decimal places for readability
df["BMI"] = df["BMI"].round(2)

# Assign Health_Status based on BMI value
def get_health_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Healthy range"
    elif bmi <= 29.9:
        return "Overweight risk"
    elif bmi <= 34.9:
        return "High risk of diabetes/heart disease"
    else:
        return "Critical health condition"

# Apply the function to each row
df["Health_Status"] = df["BMI"].apply(get_health_status)

# Display updated DataFrame
print("Updated data with BMI and Health_Status (first 10 rows):")
print(df.head(10))
print()

# Save the updated data to a new CSV file
df.to_csv("health_data_updated.csv", index=False)
print("Updated data saved to health_data_updated.csv")

# Show count of each health status
print()
print("Health Status Summary:")
print(df["Health_Status"].value_counts())
