#####
# Group Number: 136
# STUDENT NAME: Yamin Hossain
# STUDENT NUMBER: S371068
# STUDENT NAME: SALMA FARIHA EERA
# STUDENT NUMBER: S371692
# STUDENT NAME: IFROIM DEWAN
# STUDENT NUMBER: 
####
import math

# Question 1 sub-section 2
# Function to check if a password is valid based on the given criteria
def is_valid_password(password):
    for pas in password:
        print("a",pas,"b")
    # Check if password length is within the specified range
    if 11 <= len(password) <= 18:
        # Count lowercase, uppercase, digits, and special characters
        lowercase_count = sum(1 for char in password if char.islower())
        uppercase_count = sum(1 for char in password if char.isupper())
        digit_count = sum(1 for char in password if char.isdigit())
        special_count = sum(1 for char in password if char in '$#@!&;*()-_^')
        
        # Check if the password meets all criteria
        if (lowercase_count >= 2 and
            uppercase_count >= 4 and
            digit_count >= 3 and
            special_count >= 2):
            return True
    return False
#Question 1 sub-section 1
# Function to validate a list of passwords and print valid ones
def validate_passwords():
    passwords = input("Enter comma-separated passwords: ").split(',')
    valid_passwords = [password for password in passwords if is_valid_password(password)]
    output = " || ".join(valid_passwords)
    print("Valid passwords:", output)

# Question 2
# Question 2 sub-section 1
# Function to encrypt a Plain text based on the Keywords
def encrypt (plain_text, keyword):
    encrypted_text = ""
    # iterating through every character of the plain_text
    for i in range(len(plain_text)):
        # Check if the character is a capital letter
        if plain_text[i].isalpha() and plain_text[i].isupper():
            # Calculate the shift based on the position of the keyword character
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            # Apply the encryption formula and convert back to a capital letter
            encrypted_char = chr(((ord(plain_text[i]) - ord('A') + shift) % 26) + ord('A'))
              # added the encrypted char to the decrypted_text list
            encrypted_text += encrypted_char
    return encrypted_text

# Question 2 sub-section 2
# Function to Decrypt a encrypted text into Plain text based on 
def decrypt (encrypted_text, keyword):
    decrypted_text = ""
    # iterating through every character of the encrypted_text
    for i in range(len(encrypted_text)):
        # Check if the character is a capital letter
        if encrypted_text[i].isalpha() and encrypted_text[i].isupper():
            # Calculate the shift based on the position of the keyword character
            shift = ord(keyword[i%len(keyword)]) - ord("A")
            # Apply the decryption formula and convert back to a capital letter
            decrypted_char = chr((ord(encrypted_text[i])- ord("A") - shift) % 26 + ord("A"))
            # added the decrypted char to the decrypted_text list
            decrypted_text += decrypted_char
    return decrypted_text

    movements = []
    while True:
        s =input("Enter movement (Direction distance) or press enter to finish: ")
        if not s:
            break
        movement = s.split(" ")
        direction = movement[0].upper()
        step = int(movement[1])
        movements.append((direction, step))
    return movements
#  Question 3
# Function to calculate the distance of the car 
def run_distance_calculator():
    # Initialize the starting position of the car
    pos = [0, 0]
    # Loop to keep taking movement inputs until the user decides to finish
    while True:
        # Take user input for movement (format: Direction distance)
        s =input("Enter movement (Direction distance) or press enter to finish: ")
        # Break the loop if the user presses Enter
        if not s:
            break

        # Split the input into direction and distance
        movement = s.split(" ")
        direction = movement[0].upper()
        steps = int(movement[1])

        # Update the position based on the direction and distance
        if direction == "UP":
            pos[0] += steps
        elif direction == "DOWN":
            pos[0] -= steps
        elif direction == "LEFT":
            pos[1] -= steps
        elif direction == "RIGHT":
            pos[1] += steps
    # Calculate the Euclidean distance using the Pythagorean theorem
    distance = math.sqrt(pos[0] ** 2 + pos[1] ** 2)
    # Return the calculated distance
    return distance
# Question 4 sub-section 1
# Function to process the input text
def process_text(text):
    """
    Process the input text to separate numbers and characters.

    Args:
        text (str): The input text to be processed.

    Returns:
        tuple: A tuple containing two lists - numbers and characters.
    """
    numbers = []  # List to store extracted numbers
    chars = []    # List to store extracted characters
    temp_num = ""  # Temporary variable to build numeric sequences

    for char in text:
        if char.isdigit():
            temp_num += char  # If the character is a digit, add it to the temporary numeric sequence.
        else:
            if temp_num:
                numbers.append(int(temp_num))  # If a numeric sequence just ended, convert and append it.
                temp_num = ""  # Reset the temporary numeric sequence.
            if char.isalpha():
                chars.append(char)  # If the character is alphabetic, add it to the character list.

    if temp_num:
        numbers.append(int(temp_num))  # Add any remaining numeric sequence if present.

    return numbers, chars

# Question 4 sub-section 2
# Function to check if the number is prime
def is_prime(n):
    """
    Check if a given number is prime.

    Args:
        n (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False  # Numbers less than or equal to 1 are not prime.
    if n <= 3:
        return True   # 2 and 3 are prime numbers.
    if n % 2 == 0 or n % 3 == 0:
        return False  # Numbers divisible by 2 or 3 are not prime.

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False  # If divisible by any number from 5 to sqrt(n), it's not prime.
        i += 6

    return True  # If no divisors found, it's prime.

# Question 4 sub-section 3
# Function palindrome word greater than 4
def is_palindrome(word):
    """
    Check if a given word is a palindrome and has length greater than 4.
    
    Args:
        word (str): The word to be checked.
        
    Returns:
        bool: True if the word is a palindrome and longer than 4 characters, False otherwise.
    """
    return word == word[::-1] and len(word) > 4

# Main program
def main():
    while True:
        print("Select the program to run:")
        print("1. Password Validation Program")
        print("2. Encryption and Decryption Program")
        print("3. Distance Calculator")
        print("4. Palindrome Checker And PrimeSum Calculator")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            validate_passwords()
        elif choice == "2":
            # Get the input from the user
            plain_text = input("Enter the plain text: ").upper()
            keyword = input("Enter the keyword: ").upper()
            encrypted_text = encrypt(plain_text, keyword)
            decrypted_text = decrypt(encrypted_text, keyword)
            print("Encrypted text : ", encrypted_text)
            print("Decrypted text : ", decrypted_text)
        elif choice == "3":
           distance = run_distance_calculator()
           print("Distance from the original point:", distance)
        elif choice == '4':
            try:
                # Open and read the input file
                with open("input_text.txt", "r") as fs:
                    text = fs.read()
                    # Process the text to extract numbers and characters
                    numbers, chars = process_text(text)
                    
                    # Calculate the sum of individual numbers
                    num_sum = sum(numbers)
                    print(f"Sum of individual numbers: {num_sum}")
                    
                    # Check if the sum is a prime number
                    if is_prime(num_sum):
                        print(f"The sum {num_sum} is a prime number.")
                    else:
                        print(f"The sum {num_sum} is not a prime number.")
                    
                    # Concatenate characters to form the alphabet series
                    alphabet_series = "".join(chars)
                    alphabet_palindrome_found = False
                    
                    # Find palindrome words longer than 4 characters within the alphabet series
                    for i in range(len(alphabet_series)):
                        for j in range(i + 1, len(alphabet_series) + 1):
                            if is_palindrome(alphabet_series[i:j]):
                                alphabet_palindrome_found = True
                                if j - i > 4:
                                    print(f"Palindrome found in characters: {alphabet_series[i:j]}")
                    
                    # If no palindrome is found in characters
                    if not alphabet_palindrome_found:
                        print("No palindrome found in characters.")
            
            except FileNotFoundError:
                print("File not found.")
                
        elif choice == "0":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 0.")

if __name__ == "__main__":
    main()