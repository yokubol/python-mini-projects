# Import argument variable from sys module.
from sys import argv

# Unpack the argument variable.
script, input_file = argv

# Define a function that prints out all content in a file.
def print_all(f):
	print(f.read())

# Define a function that rewind to a specific point of a file.
def rewind(f):
	f.seek(0)

# Define a function that prints one specific line.
def print_a_line(line_count, f):
	print(line_count, f.readline())

# Assign an object from a file to a variable.
current_file = open(input_file)

# Tell user that the program is going to print out the whole file.
print("First let's print the whole file:\n")

# Print all content from the file using print_all function.
print_all(current_file)

# Tell user that the program is going to rewind to the position zero of the file.
print("Now let's rewind, kind of like a tape.")

# Rewind to the position zero of the file using rewind function.
rewind(current_file)

# Tell user that the program is going to print out three lines from file.
print("Let's print three lines:")

# Assign the current line to line number 1.
current_line = 1
# Print out a single line using print_a_line function.
print_a_line(current_line, current_file)

# Assign the current line to the next line.
current_line += 1
# Print out a single line using print_a_line function.
print_a_line(current_line, current_file)

# Assign the current line to the next line.
current_line += 1
# Print out a single line using print_a_line function.
print_a_line(current_line, current_file)
