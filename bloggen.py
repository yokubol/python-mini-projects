# This Program will excerpt comments from Python program
# and generate them into points

# ask user to input filename
filename = input("Enter python script's name: ")

excerptStatus = input("Is this an Excerpt? [Y/N] ")

# open file and assign the object as a variable 'target'
target = open(filename)

newblog = open("blogwrite.txt", 'w')

if excerptStatus == 'Y' or excerptStatus == 'y':
	chapter = input("From which chapter? ")
	newblog.write(f"Note: This project is an exerpt of exercise {chapter} from the book 'Learn Python The Hard Way'\n\n")

# readline
lines = target.readlines()

# read all content in file then assign to a variable 'txt'
txt = target.read()

# if 'Mary' in txt:
# 	print("success")

# print(line[2])

findtext = '#'

i = 1

for line in lines:
	if findtext in line:
		#print(line)
		line = line.replace("#", "")
		newblog.write(f"{i}.{line}")
		i += 1

newblog.write("\n")
newblog.write("Result:\n\n")
newblog.write("Source code can be found here.")

target.close()
newblog.close()