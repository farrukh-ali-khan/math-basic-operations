# Ask the user to enter the dividend (1 to 100)
dividend = int(input("Enter the dividend (1-100): "))

# Ask the user to enter the divisor (1 to 12)
divisor = int(input("Enter the divisor (1-12): "))

# Calculate the quotient using integer division
quotient = dividend // divisor

# Calculate the remainder using modulus operator
remainder = dividend % divisor

# Print the quotient
print("Quotient:", quotient)

# Print the remainder
print("Remainder:", remainder)
