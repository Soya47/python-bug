# Seriously Wrong Python Code

import os
import sys
import subprocess

def execute_command(command):
    os.system(command)

def delete_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            os.remove(os.path.join(root, file))

def vulnerable_function(input_data):
    # This function is highly vulnerable to command injection
    os.system("rm -rf " + input_data)

def insecure_password_storage(password):
    # Storing password in plain text which is highly insecure
    with open("passwords.txt", "a") as f:
        f.write(password + "\n")

def sql_injection(username, password):
    # This function is vulnerable to SQL injection
    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
    result = execute_query(query)
    return result

def execute_query(query):
    # Execute the SQL query
    # This function is incomplete and vulnerable to SQL injection
    connection = get_database_connection()
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_database_connection():
    # Function to establish database connection
    # This function is incomplete and may raise errors
    connection = psycopg2.connect(
        dbname='database',
        user='user',
        password='password',
        host='localhost',
        port='5432'
    )
    return connection

if __name__ == "__main__":
    # Main entry point of the script
    if len(sys.argv) < 2:
        print("Usage: python seriously_wrong.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "delete_files":
        directory = input("Enter directory path: ")
        delete_files(directory)
        print("Files deleted successfully!")
    elif command == "vulnerable_function":
        input_data = input("Enter data to delete: ")
        vulnerable_function(input_data)
        print("Data deleted successfully!")
    elif command == "insecure_password_storage":
        password = input("Enter password to store: ")
        insecure_password_storage(password)
        print("Password stored securely!")
    elif command == "sql_injection":
        username = input("Enter username: ")
        password = input("Enter password: ")
        result = sql_injection(username, password)
        print("Logged in successfully!" if result else "Invalid credentials!")
    else:
        print("Invalid command. Available commands: delete_files, vulnerable_function, insecure_password_storage, sql_injection")
