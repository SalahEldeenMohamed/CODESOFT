#####################################################################
# ---------------------CodeSoft Internship--------------------------#
# Created: 29/11/2023 4:12:49 PM                                    #
# Author: Salah Eldeen Mohamed Hemdan                               #
# Project: Password Generator                                       #
#####################################################################

############################ Import Section ################################
import random
import string

############################ Function Section ################################
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

############################ Program Section ################################
# Get user input for password length
try:
    length = int(input("Enter the desired length of the password: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Check if the length is greater than 0
if length > 0:
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")
else:
    print("Invalid password length. Please enter a positive integer.")
