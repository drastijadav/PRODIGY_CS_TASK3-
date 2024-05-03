import re


def check_strength(password):
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = any(c.isupper() for c in password)
    lowercase_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_character_criteria = bool(
        re.match(r'[!@#$%^&*()_+{}\[\]:;\"\'|\\<,>.?/~`]', password))

    # Assess strength based on criteria
    strength = 0
    if length_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_character_criteria:
        strength += 1

    # Provide feedback
    if strength < 3:
        return "Weak"
    elif strength < 5:
        return "Moderate"
    else:
        return "Strong"


# Example usage
password = input("Enter your password: ")
strength = check_strength(password)
print("Password strength:", strength)
