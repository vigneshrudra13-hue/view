import sqlite3

# 1. Connect to the database (creates the file if it doesn't exist)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 2. Write your SQL as a Python string and execute it
cursor.execute('''
    SELECT trips.name,trips.date, expenses.amount
    FROM trips
    INNER JOIN expenses ON trips.id = expenses.id
''')

# 3. Pull the data into Python
results = cursor.fetchall()
for row in results:
    print(row) # Now you can use this data in your game logic

# 4. Close the connection
conn.close()