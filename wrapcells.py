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
#print(first_column)
maxrow = first_column.shape

#print(maxrow, maxrow[0])
currentRow=1
print(f'(', end=" ")
# Iterate over the cells in the first column and print them
for cell in first_column:
    if  (currentRow<maxrow[0]):
        print(f'"{cell}",' , end=" ")
    else:
        print(f'"{cell}")', end=" ")
    currentRow+=1