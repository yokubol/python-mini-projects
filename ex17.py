# Import argument variable argv from sys module.
from sys import argv
# Unpack the argument variable 'argv'.
script, from_file, to_file = argv

# Tell user that program is going to copy all contents from
# the original file to the newly created file.
print(f"Copying from {from_file} to {to_file}")

# Open file. Then read the file. 
# Then assign the string in a variable 'data'.
indata = open(from_file).read()

# Open a newly-created file in write mode.
out_file = open(to_file, 'w')
# Write string from 'indata' into the newly-created file.
out_file.write(indata)

print("Alright, all done.")

# Close the written file.
out_file.close()