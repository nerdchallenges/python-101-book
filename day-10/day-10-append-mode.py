# Access Modes (append) with Python!

# Access Modes with the open(arguments)
# r - Read Mode
# a - Append Mode
# w - Write Mode
# x - Create Mode

# Example 1 - Refresher
names_file = open("more_names.txt", "r")
print(names_file.readable())
names_file.close()

# Example 2 - Append to existing file
names_file = open("more_names.txt", "a")
names_file.write("\nGates")
names_file.close()
names_file = open("more_names.txt", "r")
print(names_file.read())
names_file.close()

# Example 3 - File that does not exist
names_file = open("random.txt", "a")
names_file.write("\nGates")
names_file.close()
names_file = open("random.txt", "r")
print(names_file.read())
names_file.close()

# Example 4 - Combine files: nerd_names + more_names.txt
names_file = open("more_names.txt", "a")
nerd_file = open("nerd_names.txt", "r")

# Append the nerd_names.txt content to more_names.txt
names_file.write(nerd_file.read())

# Alec Baldwin says Always be closing :D
nerd_file.close()
names_file.close()

# Open names_file to read
names_file = open("more_names.txt", "r")
print(names_file.read())

# Close again
names_file.close()

