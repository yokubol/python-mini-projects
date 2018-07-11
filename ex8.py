# assign a variable as a formatted string with 4 substitutable brackets
formatter = "{} {} {}"
# display numbers on the screen using formatted string
print(formatter.format(1, 2, 3, 4))
# display words on the screen using formatted string
print(formatter.format("one", "two", "three", "four"))
# display boolean values on the screen using formatted string
print(formatter.format(True, False, False, True))
# insert formatter into formatted strings and display on the screen
print(formatter.format(formatter, formatter, formatter, formatter))
# insert phrases into formatters and display them on the screen
print(formatter.format(
	"Try your",
	"Own text here",
	"Maybe a poem",
	"Or a song about fear"
))