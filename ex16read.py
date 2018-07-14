# import argument variable from sys module
from sys import argv

# unpack the argument variable
script, filename = argv

# open file using open then assign the object into a variable 'target'
target = open(filename)

# tell user that program is going to display all content from the file
print(f"Program {script} is going to read {filename}.")
print("Press RETURN to continue.")

# prompt user before continue
input("?")

# read all content from file then assign it into a variable 'txt'
txt = target.read()
# display all content from file
print(txt)

# close file
target.close()