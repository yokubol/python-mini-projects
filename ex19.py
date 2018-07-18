# Define a function named 'cheese_and_crackers'
# which tells how many cheeses and crackers we have.
# This function has 2 arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print(f"You have {cheese_count} cheeses!")
	print(f"You have {boxes_of_crackers} boxes of crackers!")
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


print("we can just give the function numbers directly:")
# Assign arguments for cheese and cracker and get the function run.
cheese_and_crackers(20, 30)


# Assign variables directly in the script for later use in the function.
print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# Get the function run with assigned variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# Run a function with math statement as arguments.
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# Run a function with math statements and variables together as arguments.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def haha(number_1, number_2, string_1, string_2):
	print(f"First number: {number_1}")
	print(f"Second number: {number_2}")
	print(f"First string: {string_1}")
	print(f"Second string: {string_2}\n")

haha(1, 2, 'a', 'b')
haha(1+2, 33, 'jo', 'bim')
haha(3, 3**5, 'jo'+'ny', 'i'+'vy')

constant_1 = 3
constant_2 = 32
text_1 = "This is sparta"

haha(constant_1, 32, 'jo', 'ka')
haha(constant_1 + constant_2, 3, 'baka', 'cheerka')
haha(constant_2 * 30, 78, 'bo', 'jo')
haha(32, 30, f"cho {constant_1}", 'bim')
haha(3, 32, constant_1, constant_2)
haha(25, 78, text_1, text_1)
haha(32, constant_2, text_1, 'bio')