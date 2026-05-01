import os
import sqlite3

# Hardcoded secret (security issue)
API_KEY = "12345-SECRET-KEY"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # SQL Injection vulnerability
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()

# Command injection risk
def run_command(cmd):
    os.system(cmd)

if __name__ == "__main__":
    user = input("Enter username: ")
    print(get_user(user))
