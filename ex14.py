# import sys module
from sys import argv
# unpack an argument variable
script, user_name, password = argv
# assign a prompt line as a variable
prompt = 'Answer: '
# display welcome message with user's name and script's name
print(f"Hi {user_name}, I'm the {script} script. Your password is {password}.")
# display a sentence before asking a few questions
print("I'd like to ask you a few questions.")
# display a question asking user about liking
print(f"Do you like me {user_name}?")
# have an input and assign the input as a variable'likes'
likes = input(prompt)

# display a question about city, which user's living
print(f"Where do you live {user_name}?")
# have an input and assign the input as a variable 'lives'
lives = input(prompt)

# display a question asking about user's computer
print("What kind of computer do you have?")
# prompt for an input and assign the input as a variable 'computer'
computer = input(prompt)

# display all information in complete sentences
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you have a {computer} computer.  Nice.
""")