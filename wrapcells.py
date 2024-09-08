import pandas as pd
import sys

# Ask the user for the Excel file name
#file_name = input("Please enter the name of the Excel file: ")

#print(sys.argv)

file_name = sys.argv[1]
# Load the Excel file
df = pd.read_excel(file_name, header=None)

# Get the first column (assuming it is labeled 'A' or is the first column)
first_column = df.iloc[:, 0]
print("(", ','.join([f'{i}'  for i in first_column]), ")")
