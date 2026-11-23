import secrets
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (minimum 4): "))

    if length < 4:
        print("Password length must be at least 4.")
    else:
        uppercase = string.ascii_uppercase
        lowercase = string.ascii_lowercase
        digits = string.digits
        symbols = "!@#$%&*?"

        # Include at least one character from each group
        password_chars = [
            secrets.choice(uppercase),
            secrets.choice(lowercase),
            secrets.choice(digits),
            secrets.choice(symbols)
        ]

        all_chars = uppercase + lowercase + digits + symbols

        # Fill the remaining positions
        for i in range(length - 4):
            password_chars.append(secrets.choice(all_chars))

        # Mix the characters into a random order
        secrets.SystemRandom().shuffle(password_chars)

        password = "".join(password_chars)
        print("Generated password:", password)

except ValueError:
    print("Please enter a whole number.")
