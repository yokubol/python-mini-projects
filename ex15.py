# import sys module for using argv later
from sys import argv
# use argv to get a filename
script, filename = argv
# open the file and assign objects in the file into variable 'txt'
txt = open(filename)
# tell user a name of the file in a complete sentence
print(f"Here's your file {filename}:")
# display file's content using read function
print(txt.read())
# close file
txt.close()

# tell user to enter the filename again
print("Type the filename again:")
# prompt for an answer and assign what user has entered as a variable 'file_again'
file_again = input("> ")
# open the file and assign objects in the file into variable 'txt_again'
txt_again = open(file_again)

# display file's content using read function
print(txt_again.read())

#close file
txt_again.close()