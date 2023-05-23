import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('merito.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS jobs")

# Creating table
table = """ CREATE TABLE jobs (
            Title VARCHAR(255) NOT NULL,
            Company CHAR(25) NOT NULL,
            Link CHAR(255),
            Mode CHAR(255),
            Experience CHAR(25),
            Location CHAR(255)
        ); """

cursor_obj.execute(table)
cursor_obj.execute("SELECT * FROM jobs")

rows = cursor_obj.fetchall()

for row in rows:
    print("hello")
    print(row)

print("Table is Ready")

# Close the connection
connection_obj.close()