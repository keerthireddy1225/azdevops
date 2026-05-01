import os
import sqlite3

# Hardcoded secret (security issue)
API_KEY = "123456-SECRET-KEY"
# Simulated real API key (this WILL trigger push protection)
GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz1234567890"

# AWS-style secret (also detected)
AWS_SECRET_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLESECRETKEY12345"

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
