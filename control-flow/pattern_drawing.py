# pattern_drawing.py

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) to control the rows
while row < size:
    # Inner loop (for) to print asterisks in the row
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after one row
    row += 1
