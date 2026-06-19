import os

# Use environment variable for secret
API_KEY = os.getenv('API_KEY')

def get_user(user_id):
    # Parameterized query to prevent SQL injection
    query = "SELECT * FROM users WHERE id = %s"
    return execute_query(query, (user_id,))

def process_data(data):
    try:
        result = data["key"]["nested"]["value"]
    except KeyError:
        result = None
    with open("/tmp/output.txt", "w") as file:
        file.write(str(result))

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
