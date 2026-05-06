import sqlite3

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT,
    password TEXT
)
""")

# Insert sample user
cursor.execute("INSERT INTO users VALUES ('admin', 'admin123')")
conn.commit()

print("=== Vulnerable Login System ===")

username = input("Enter Username: ")
password = input("Enter Password: ")

# VULNERABLE SQL QUERY
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"

print("\nExecuting Query:")
print(query)

cursor.execute(query)

result = cursor.fetchone()

if result:
    print("\nLogin Successful!")
else:
    print("\nInvalid Credentials!")

conn.close()
