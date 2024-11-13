users = {
    'admin': {'password': 'admin123', 'role': 'Admin'},
    'user': {'password': 'user123', 'role': 'User'}
}

def login(username, password):
    
    if username in users and users[username]['password'] == password:
        return users[username]['role']
    else:
        raise ValueError("\nInvalid username or password")

