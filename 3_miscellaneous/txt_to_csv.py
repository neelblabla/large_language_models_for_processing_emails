"""
Script to turn the nested folder structure of thousands
of folders and .txt-files into a single .csv-file.
"""

# Importing necessary libraries
import os
import pandas as pd

# Defining the folder where the enron emails are located
folder_path = '../maildir'

# Initializing an empty list to store the contents of each enron email
file_contents = []

# Iterating through the subfolders and files in the main folder
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # Check if the file has a .txt extension
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            # Only get the email content if there is no utf-8 encoding error
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    file_contents.append(content)
            except UnicodeDecodeError:
                continue

# Creating a DataFrame from the list of enron emails
df = pd.DataFrame({'RawMailContent': file_contents})

# Saving the final DataFrame
df.to_csv("../enron_mails.csv", index=False)

# Saving a subsample of 5000 emails
df_short = df.sample(n=5000)
df_short.to_csv("../enron_mails_subsample.csv", index=False)

print("Enron email dataset and 5000-row-subset successfully created.")