def validate_password(password):
    # Check the length of the password.
    if len(password) < 8:
        return False

    # Initialize flags for uppercase, lowercase, and digit presence.
    has_upper = False
    has_lower = False
    has_digit = False

    # Check each character in the password.
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

        # Check for spaces.
        if char.isspace():
            return False

    # Return True if all conditions are met.
    return has_upper and has_lower and has_digit

print(validate_password("Password123"))
print(validate_password("abc123"))
print(validate_password("Password 123"))
print(validate_password("password123")) 