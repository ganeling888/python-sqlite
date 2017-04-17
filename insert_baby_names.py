import os
import sqlite3
os.chdir(os.getcwd() + '/namesbystate')

import csv
# Create a connection to the database at the file path specified above
conn = sqlite3.connect('../' + 'babynamedb.db')
# Cursor object to fetch data from database and maintain pointer to result sets
c = conn.cursor()
# For each file in the current working directory (modified by any chdir call above)
for filename in os.listdir(os.getcwd()):
    # Open each file in universal read mode, and alias as csvfile for manipulation
    with open(filename, 'rU') as csvfile:
        # Fieldnames represent the eventual column names of the database
        fieldnames = ['state', 'sex', 'year_of_birth', 'name', 'number']
        # https://docs.python.org/3/library/csv.html#csv.DictReader
        reader = csv.DictReader(csvfile, fieldnames=fieldnames)
        # Go through every row that was loaded from CSV
        for row in reader:
            # Inserting the records into the database
            c.execute("INSERT INTO baby_name (state,gender,year,name,number)
            VALUES (?,?,?,?,?);", (row['state'], row['sex'],
            row['year_of_birth'], row['name'], row['number']))
        # Commit every transaction to the database
        conn.commit()
# Close the database connection
conn.close()
# Alternative without csv module

# Create a class that maps fieldnames to integer values (Enum in python 3+)
'''
class Baby_Name():
    STATE = 0
     SEX = 1
     YEAR_OF_BIRTH = 2
     NAME = 3
     NUMBER = 4

# Get all of the file names from the namesbystate
# For each file in the directory of the current working directory
for filename in os.listdir(os.getcwd()):
    # Open the file descriptor associated with the filename
    file = open(filename, "r")
    # for each line in the newly opened file descriptor
    for line in file:
        # Create an array of all token delimited string
        currentline = line.split(",")
        c.execute("INSERT INTO baby_name (state,gender,year,name,number)
         VALUES (?,?,?,?,?);", (currentline[Baby_Name.STATE],
         currentline[Baby_Name.SEX], currentline[Baby_Name.YEAR_OF_BIRTH],
         currentline[Baby_Name.NAME], currentline[Baby_Name.NUMBER]))
    conn.commit()
conn.close()
'''
