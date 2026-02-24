import random
import string

def generate_password(length=12, use_special_chars=True):
    """
    Generates a strong, random password with a mix of letters, digits, and symbols.
    """
    # Minimum length enforcement
    if length < 6:
        print("Warning: Password length must be at least 6. Setting length to 6.")
        length = 6

    # Define character pools
    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits          # 0-9
    special = string.punctuation    # !@#$%^&*...

    # Base pool (Always include letters and digits)
    char_pool = letters + digits
    
    # Add special characters if requested
    if use_special_chars:
        char_pool += special

    password = []
    
    # Ensure at least one of each required type exists
    password.append(random.choice(string.ascii_lowercase))
    password.append(random.choice(string.ascii_uppercase))
    password.append(random.choice(string.digits))
    
    if use_special_chars:
        password.append(random.choice(special))

    # Fill the remaining length
    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(char_pool))

    # Shuffle the list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return
    return "".join(password)

def main():
    print("--- 🔒 Secure Password Generator (By Will) ---")
    print("Generates high-entropy passwords for better security.\n")
    
    try:
        user_input = input("Enter password length (Default: 12): ")
        if not user_input:
            length = 12
        else:
            length = int(user_input)
    except ValueError:
        print("Invalid input! Using default length of 12.")
        length = 12

    print("\nGenerated Passwords:")
    print("-" * 30)
    
    # Generate 3 options
    for i in range(3):
        pwd = generate_password(length)
        print(f"Option {i+1}: {pwd}")
    
    print("-" * 30)
    print("Tip: Keep your passwords safe and use a manager!")

if __name__ == "__main__":
    main()