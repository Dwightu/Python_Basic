users = [
    (0, "Bob", "Password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

username_mapping = {user[1]: user[2] for user in users}

print(username_mapping)
