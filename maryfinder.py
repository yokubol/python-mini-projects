# This Program will excerpt comments from Python program
# and generate them into points

# ask user to input filename
filename = input("Enter python script's name: ")

# open file and assign the object as a variable 'target'
target = open(filename)

# read all content in file then assign to a variable 'txt'
txt = target.read()

if 'Mary' in txt:
	print("success")

target.close()