import math

def fruit_exchange(name_1, name_2, amount_of_apple, amount_of_orange, apple_exchange_rate):
	orange_apple_poolratio = amount_of_orange / amount_of_apple
	exchanged_apple = amount_of_orange / apple_exchange_rate
	exchanged_orange = exchanged_apple * apple_exchange_rate


	print(f"{name_1}: Hello {name_2}, let's exchange our fruits.")
	print(f"{name_2}: Hi {name_1}, I have {amount_of_orange} oranges. How many apples do you have?")
	print(f"{name_1}: I have {amount_of_apple} apples. One apple is worth {apple_exchange_rate} oranges.")

	if apple_exchange_rate <= amount_of_orange and apple_exchange_rate >= 1 / amount_of_apple:
		if orange_apple_poolratio < apple_exchange_rate:
			exchanged_orange = amount_of_orange
			exchanged_apple = math.floor(exchanged_orange / apple_exchange_rate)
			exchanged_orange = exchanged_apple * apple_exchange_rate
			print(f"{name_2}: Then you receive {exchanged_orange} oranges. Now I have {exchanged_apple} apples and {amount_of_orange - exchanged_orange} oranges.")
			print(f"{name_1}: Yeah, and now I have {amount_of_apple - exchanged_apple} apples and {exchanged_orange} oranges.\n")
		elif orange_apple_poolratio > apple_exchange_rate:
			exchanged_apple = amount_of_apple
			exchanged_orange = math.floor(exchanged_apple * apple_exchange_rate)
			print(f"{name_2}: Then you receive {exchanged_orange} oranges. Now I have {exchanged_apple} apples and {amount_of_orange - exchanged_orange} oranges.")
			print(f"{name_1}: Yeah, and now I have {amount_of_apple - exchanged_apple} apples and {exchanged_orange} oranges.\n")
		else:
			exchanged_apple = amount_of_apple
			exchanged_orange = amount_of_orange
			print(f"{name_2}: Then you receive {exchanged_orange} oranges. Now I have {exchanged_apple} apples and {amount_of_orange - exchanged_orange} oranges.")
			print(f"{name_1}: Yeah, and now I have {amount_of_apple - exchanged_apple} apples and {exchanged_orange} oranges.\n")
	else:
		print(f"{name_2}: We cannot exchange!\n")


	
	

	# print("----Exchange status----")
	# print(f"Oranges per apple exhange rate: {apple_exchange_rate}")
	# print(f"Oranges per apple pool ratio: {orange_apple_poolratio}\n")
	# print(f"Apple: {amount_of_apple}")
	# print(f"Orange: {amount_of_orange}\n")

	# if orange_apple_poolratio < apple_exchange_rate:
	# 	print("Too many apples\n")
	# elif orange_apple_poolratio > apple_exchange_rate:
	# 	print("Too many oranges\n")
	# else:
	# 	print("All exchanged!\n")

	# if orange_apple_poolratio < apple_exchange_rate:
	# 	exchanged_orange = amount_of_orange
	# 	exchanged_apple = exchanged_orange / apple_exchange_rate
	# 	print(f"Exchanged oranges: {exchanged_orange}")
	# 	print(f"Exchanged apples: {exchanged_apple}\n")
	# elif orange_apple_poolratio > apple_exchange_rate:
	# 	exchanged_apple = amount_of_apple
	# 	exchanged_orange = exchanged_apple * apple_exchange_rate
	# 	print(f"Exchanged oranges: {exchanged_orange}")
	# 	print(f"Exchanged apples: {exchanged_apple}\n")
	# else:
	# 	exchanged_apple = amount_of_apple
	# 	exchanged_orange = amount_of_orange
	# 	print(f"Exchanged oranges: {amount_of_orange}")
	# 	print(f"Exchanged apples: {amount_of_apple}\n")


fruit_exchange('John', 'Mike', 10, 20, 0.4598)
fruit_exchange('Mary', 'Jane', 30, 23, 3)
fruit_exchange('Bigot', 'Cowboy', 32, 300, 344)
fruit_exchange('Manny', 'Susy', 458, 5, 1)