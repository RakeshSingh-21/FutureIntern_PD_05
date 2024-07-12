import random
import string

def generate_password(length, has_uppercase, has_lowercase, has_numbers, has_special_chars):
    password = []
    char_sets = []

    if has_uppercase:
        char_sets.append(string.ascii_uppercase)
    if has_lowercase:
        char_sets.append(string.ascii_lowercase)
    if has_numbers:
        char_sets.append(string.digits)
    if has_special_chars:
        char_sets.append(string.punctuation)

    for _ in range(length):
        char_set = random.choice(char_sets)
        password.append(random.choice(char_set))

    random.shuffle(password)
    return ''.join(password)
def main():
    print("Random Password Generator")
    print("-------------------------")

    length = int(input("Enter the desired password length: "))

    has_uppercase = input("Include Uppercase letters? (y/n): ").lower() == 'y'
    has_lowercase = input("Include Lowercase letters? (y/n): ").lower() == 'y'
    has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    has_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, has_uppercase, has_lowercase, has_numbers, has_special_chars)

    print("Generated Password: ", password)

if __name__ == "__main__":
    main()