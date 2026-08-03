user_input = input("Enter a string: ")

# Define vowels (including both lowercase and uppercase)
vowels = "aeiouAEIOU"

# Initialize an empty string for the result
new_string = ""

# Iterate over each character in the input string
for char in user_input:
    if char in vowels:
        new_string += "*"
    else:
        new_string += char

print(new_string)   