import os

# Hardcoded secret (security issue)
API_KEY = "sk-1234567890abcdef"

def get_user(user_id):
    # SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id}"
    return execute_query(query)

def process_data(data):
    # No error handling
    result = data["key"]["nested"]["value"]
    file = open("/tmp/output.txt", "w")
    file.write(str(result))
    # File handle never closed

def divide(a, b):
    # No zero division check
    return a / b
