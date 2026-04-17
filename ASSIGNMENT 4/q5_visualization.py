"""
This program reads health_data.csv using Pandas and creates scatter
plots for: weight vs height, age vs weight, height vs age,
gender vs height, and gender vs weight using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("health_data.csv")

print("Data loaded successfully.")
print("First 5 rows:")
print(df.head())
print()

# Plot 1: Weight vs Height
plt.figure()
plt.scatter(df["height"], df["weight"], color="blue")
plt.title("Weight vs Height")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.savefig("plot1_weight_vs_height.png")
plt.show()
print("Plot 1 saved: weight vs height")

# Plot 2: Age vs Weight
plt.figure()
plt.scatter(df["age"], df["weight"], color="green")
plt.title("Age vs Weight")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.savefig("plot2_age_vs_weight.png")
plt.show()
print("Plot 2 saved: age vs weight")

# Plot 3: Height vs Age
plt.figure()
plt.scatter(df["age"], df["height"], color="red")
plt.title("Height vs Age")
plt.xlabel("Age")
plt.ylabel("Height")
plt.savefig("plot3_height_vs_age.png")
plt.show()
print("Plot 3 saved: height vs age")

# Plot 4: Gender vs Height
# Convert gender to numeric for scatter plot (Male=1, Female=0)
df["gender_num"] = df["gender"].map({"Male": 1, "Female": 0})

plt.figure()
plt.scatter(df["gender_num"], df["height"], color="purple")
plt.title("Gender vs Height")
plt.xlabel("Gender (0=Female, 1=Male)")
plt.ylabel("Height")
plt.xticks([0, 1], ["Female", "Male"])
plt.savefig("plot4_gender_vs_height.png")
plt.show()
print("Plot 4 saved: gender vs height")

# Plot 5: Gender vs Weight
plt.figure()
plt.scatter(df["gender_num"], df["weight"], color="orange")
plt.title("Gender vs Weight")
plt.xlabel("Gender (0=Female, 1=Male)")
plt.ylabel("Weight")
plt.xticks([0, 1], ["Female", "Male"])
plt.savefig("plot5_gender_vs_weight.png")
plt.show()
print("Plot 5 saved: gender vs weight")

print()
print("All plots created successfully.")
