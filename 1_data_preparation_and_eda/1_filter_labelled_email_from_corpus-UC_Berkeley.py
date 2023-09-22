"""
Script to create a labelled df using UC Berkeley System.
"""

# Import of necessary libraries
import pandas as pd

# Load the CSV file
df = pd.read_csv("../brianray-enron-email-dataset/data/enron_05_17_2015_with_labels_v2.csv", low_memory=False)

# Filter rows where column "labeled" is "True"
df_filtered = df[df["labeled"] == True]

# Now, "df_filtered" contains the filtered rows with "True" in column "labeled"
df_filtered.to_csv("../labelled_enron.csv", index=False)