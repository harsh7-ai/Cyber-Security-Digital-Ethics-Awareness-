import string

def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak Password"

    elif score <= 4:
        return "Moderate Password"

    else:
        return "Strong Password"


password = input("Enter a password to check: ")

print("Password Status:", check_password(password))
