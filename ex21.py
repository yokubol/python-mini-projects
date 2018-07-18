# Define a function that adds up two numbers.
def add(a, b):
	print(f"ADDING {a} + {b}")
	return a + b

# Define a function that subtracts two numbers.
def subtract(a, b):
	print(f"SUBTRACTING {a} - {b}")
	return a - b

# Define a function that multiplies two numbers.
def multiply(a, b):
	print(f"MULTIPLYING {a} * {b}")
	return a * b

# Define a function that devides two numbers.
def devide(a, b):
	print(f"DEVIDING {a} / {b}")
	return a / b

# Tell user that program is going to do math.
print("Let's do some math with just functions!")

# Use the add function to add 30 with 5 
# then assign the value to a variable 'age'.
age = add(30, 5)
# Use the subtract function to subtract 4 from 78
# then assign the value to a variable 'height'.
height = subtract(78, 4)
# Use the multiply function to multiply 90 with 2
# then assign the value to a variable 'weight'.
weight = multiply(90, 2)
# Use the devide function to devide 100 with 2
# then assign the value to a variable 'iq'.
iq = devide(100, 2)

# Print out a sentence to tell variable age, height, weight, iq.
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Tell user that program is going to print out a puzzle.
print("Here is a puzzle.")

# Use the functions to do: age + (height - weight * iq / 2)
what = add(age, subtract(height, multiply(weight, devide(iq, 2))))
# Do: age + (height - weight * iq / 2) without using those functions.
what_2 = age + (height - weight * iq / 2)

# Tell user the calculated values from the above lines.
print("That becomes: ", what, "Can you do it by hand?")
print("That becomes: ", what_2, "Can you do it by hand?")

# Assign variables needed for later calculations.
base = 3
tall = 5

# Define a function 'find_area' that calculates an area of a triangle.
def find_area(base_value, tall_value):
	return 0.5 * base_value * tall_value

# Tell user the area of a triangle using the 'find_area' function.
print(f"The area is {find_area(base, tall)}")
# Tell user the area of a triangle using the 'multiply' function.
print(f"The area is {multiply(0.5, multiply(base, tall))}")