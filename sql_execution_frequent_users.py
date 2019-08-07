# This python file opens and executes the SQL commands listed in 'sqlite_commands.sql'
# See 'SQLite_Query.ipynb' for a detailed breakdown of the logic behind the commands

# Imports the necessary libraries, connects to the 'testdb.db' database, and creates
# a cursor
import sqlite3 
import pandas as pd
connection = sqlite3.connect(r'ProgrammerTest/testdb.db')
cursor = connection.cursor()

# Opens the .sql file with the main SQL command for entering the most frequent users
# into the 'frequent_browsers' table
sql_file = open("./sqlite_commands.sql", 'r')
sql = sql_file.read() # Obtains the SQL command from the 'sqlite_commands.sql' file
cursor.executescript(sql) # Runs the SQL command
sql_file.close() # Closes the SQL file

connection.commit() # Commits the changes to the 'frequent_browsers' table

# This function takes in a SQL query and returns the result
# as a pandas dataframe
def create_pandas_table(sql_query, database = connection):
    table = pd.read_sql_query(sql_query, database)
    return table

print('\nTable: frequent_browsers\n')

print(create_pandas_table('''SELECT * from frequent_browsers;'''))

print("\n")