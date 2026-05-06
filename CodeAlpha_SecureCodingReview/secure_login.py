import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

print("=== Secure Login System ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

# SECURE PARAMETERIZED QUERY
query = "SELECT * FROM users WHERE username = ? AND password = ?"

cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("\nLogin Successful!")
else:
    print("\nInvalid Credentials!")

conn.close()