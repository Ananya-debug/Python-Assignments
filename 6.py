
class UsernameNotUniqueError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass


def validate_user(user, existing_users):
    username, email, age = user

    if username in existing_users:
        raise UsernameNotUniqueError(f"Username '{username}' is already taken.")

    if not isinstance(age, int) or age <= 0:
        raise InvalidAgeError(f"Invalid age '{age}' for user '{username}'. Age must be a positive integer.")

    if age < 16:
        raise UnderAgeError(f"User '{username}' is under 16. Cannot add to directory.")


    if '@' not in email or '.' not in email.split('@')[-1]:
        raise InvalidEmailError(f"Invalid email '{email}' for user '{username}'.")

    return True



user_data = [
    ("john", "john@example.com", 20),
    ("alice", "alice[at]example.com", 25),    
    ("bob", "bob@example.com", -5),            
    ("john", "john.doe@example.com", 30),     
    ("eve", "eve@example.com", 15),            
    ("charlie", "charlie@example.com", 19)
]

user_directory = {}  

for user in user_data:
    try:
        if validate_user(user, user_directory):
            username, email, age = user
            user_directory[username] = email
            print(f"User '{username}' added successfully.")
    except UsernameNotUniqueError as e:
        print("Error:", e)
    except InvalidAgeError as e:
        print("Error:", e)
    except UnderAgeError as e:
        print("Error:", e)
    except InvalidEmailError as e:
        print("Error:", e)

print("\nFinal User Directory:")
print(user_directory)
