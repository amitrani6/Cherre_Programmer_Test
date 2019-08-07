# Cherre_Programmer_Test
A sample SQLite query challenge to test SQL and Python skills.

The task: Given a SQL database containing tables of information about users and website visits output the top ten users who visited the most sites.

# Repository Contents
The following 7 files and 2 folders are in this repository:

1. `ProgrammerTest/` - A folder containing the original database file **testdb.db** and instructions file **instructions.md**
2. `database_after_sql_commands/` A folder containing the database file after the SQL command was executed
3. **.gitignore** - Contains the files excluded from this repository 
4. **README.md** - This document
5. **SQLite_Query.ipynb** - A Jupyter Notebook outlining my thought process as I wrote the SQL command
6. **environment.yml** - A file for replicating the environment required to run **sql_execution_frequent_users.py**
7. **requirements.txt** - The requirements file for running **sql_execution_frequent_users.py**
8. **sql_execution_frequent_users.py** - The python script that applies the SQL command to the database
9. **sqlite_commands.sql** - A file that contains the SQL command

# Notes About The Repository
The Jupyter Notebook file **SQLite_Query.ipynb** contains the summary of the **testdb.db** file in addition to the output of the SQL commands. When opened **sql_execution_frequent_users.py** will first apply the SQL command from **sqlite_commands.sql**, then commit the changes to the database file, and lastly output the results.

# Running The SQL Command
The instructions are as follows:

1. Download this repository to your local machine
2. Replicate the environment/Install the necessary libraries using your environment/package manager
    -I use Anaconda and Pip, the instructions are in the following section
3. In command prompt/terminal enter the environment you replicated in Step 2 and run **sql_execution_frequent_users.py**

# Creating The Environment/Install The Necessary Packages
The **environment.yml** and **requirements.txt** files are included to ensure that the SQL code will run on this downloaded repository consistently regardless of your system.

## Utilizing requirements.txt Without Creating An Environment:
1. Navigate to the downloaded repository in command prompt/terminal
2. Enter the command `pip install –r requirements.txt`
3. Run the **sql_execution_frequent_users.py** file by typing `python sql_execution_frequent_users.py`

## Utilizing environment.yml To Create An Environment With Conda:
1. Navigate to the downloaded repository in command prompt/terminal
2. Enter the following commands:

      Command 1: ` conda env create -f environment.yml`
          
      Command 2: `conda activate Cherre_Programmer_Test`
          
3. Run the **sql_execution_frequent_users.py** file by typing `python sql_execution_frequent_users.py`
