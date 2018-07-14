# import argument variable from sys module
from sys import argv

# unpack the argument variable
script, filename = argv

# tell user that the program is going erase all content from file
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# prompt for an input
input("?")

# tell user that program is going to open file
print("Opening the file...")
# open file in write mode then assign as a variable
target = open(filename, 'w')

# tell user that program is now truncating the file
print("Truncating the file.  Goodbye!")
# delete all content of the file using truncate
target.truncate()

# tell user that program is going to ask user to enter 3 lines
print("Now I'm going to ask you for three lines.")

# prompt user to enter 3 lines then assign it into variables
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# tell user that program is going to write those 3 lines into the file
print("I'm going to write these to the file.")

# write 3 lines into the file
target.write(f"{line1}\n{line2}\n{line3}\n")

# close the file
print("And finally, we close it.")
target.close()
