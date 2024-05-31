import os

# Dictionary to map number words to their digit equivalents
number_words = {
    'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}

# Function to extract the required two-digit number from a line
def extract_two_digit_number(line):
    first_digit = None
    last_digit = None
    
    # Split line into words to check for number words
    words = line.split()
    
    for word in words:
        if word in number_words:
            digit = number_words[word]
            if first_digit is None:
                first_digit = digit
            last_digit = digit
    
    # Check for numeric characters in the line
    for char in line:
        if char.isdigit():
            if first_digit is None:
                first_digit = char
            last_digit = char
    
    if first_digit is not None and last_digit is not None:
        return int(first_digit + last_digit)
    return 0

# Function to process the file and calculate the sum
def calculate_sum_from_file(file_path):
    total_sum = 0
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return total_sum
    
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            number = extract_two_digit_number(line)
            total_sum += number
    
    return total_sum

# Path to the input file
file_path = '060.txt'  # Make sure this path matches where you saved the file

# Calculation of the sum and print the result
result = calculate_sum_from_file(file_path)
print("The sum of the two-digit numbers from the file is:", result)
