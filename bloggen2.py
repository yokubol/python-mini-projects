# This Program will excerpt comments from Python program
# and generate them into points

filename = input("Enter python script's name: ")

excerpt_status = input("Is this an Excerpt? [Y/N] ")

# Open file and assign the object as a variable 'target'
target = open(filename, 'r')

newblog = open("blogwrite.txt", 'w')

if excerpt_status == 'Y' or excerpt_status == 'y':
	chapter = input("From which chapter? ")
	newblog.write(f"Note: This project is an exerpt of exercise {chapter} from the book 'Learn Python The Hard Way'\n\n")

lines = target.readlines()

# Read all content in file then assign to a variable 'txt'
txt = target.read()

findtext = '#'

index = 1
line_current_hashtag = 0
line_current_find_loop = 0

newblog.write("In this project we will do the following:\n")

# Use for loop to scan through lines.
for line in lines:
	line_current_find_loop += 1
	if findtext in line:
		line = line.replace("#", "")
		# If it is the first comment, print 1. and texts
		if line_current_find_loop == 1:
			newblog.write(f"1.{line}")
			index += 1

		# If it is a block comment, print together.
		if line_current_find_loop - line_current_hashtag == 1:
			# Print only when number of line is greater than 1
			if line_current_find_loop > 1:
				newblog.write(f"{line}".lstrip())
		else:
			newblog.write(f"{index}.{line}")
			index += 1

		line_current_hashtag = line_current_find_loop

		
newblog.write("\n")
newblog.write("Result:\n\n")
newblog.write("Source code")

target.close()
newblog.close()