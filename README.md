# Utility 

This script takes the first column in an excel file and wraps each cell in quotes (") and then adds a colon to separate each cell from the next.  all the values are wrapped in parenthesys and are printed as a single row

#prerequisites:

- Install python
- run:   **pip install pandas**
- run:   **pip install openpyxl**
- download wrapcells.py  into a local folder on the PC

#To run:
- Place an excel file in the same folder as the python file
- run:  **python wrapcells.py input.xlsx**

#Example:
in the excel contains :

22222<br>
22222<br>
324234<br>
34234<br>
234234234<br>
234234<br>

The output will be

**C:\> python wrapcells.py input.xlsx
( "22222", "3434243", "324234", "34234", "234234234", "234234")**


