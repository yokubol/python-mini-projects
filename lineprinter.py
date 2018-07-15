"""This program prints out line number of a comment line.
This program is not complete."""
from sys import argv

script, filename = argv

find_string = '#'

target = open(filename, 'r')

lines = target.readlines()

for line in lines:
	if find_string in line:
		print(target.line)
