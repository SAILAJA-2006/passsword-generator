import random
import string

# Function to generate a random password
def generate_password(length, use_uppercase, use_numbers, use_special_chars):
    # Base characters
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation
    
    # Combine the available characters based on user input
    characters = lowercase
    if use_uppercase:
        characters += uppercase
    if use_numbers:
        characters += numbers
    if use_special_chars:
        characters += special_chars
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function to interact with the user
def main():
    # Get user input for password length and criteria
    length = int(input("Enter password length (e.g., 12): "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    # Display the result
    print("\nGenerated Password:", password)

if _name_ == "_main_":
    main()
