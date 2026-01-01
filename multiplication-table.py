# Ask the user to enter a number between 1 and 12
number = int(input("Enter a number (1-12): "))

# Use a loop to print the table up to 10
for i in range(1, 11):
    # Multiply the number with i and print the result
    print(number, "x", i, "=", number * i)
