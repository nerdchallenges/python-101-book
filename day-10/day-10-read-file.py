# Reading files

# Example 1 - Open and closing files.
nerd_file = open("nerd_names.txt")
nerd_file.close()

# Example 2 - Is the file readable?
nerd_file = open("nerd_names.txt")
print(nerd_file.readable())
nerd_file.close()

# Example 3 - Read the file, with readlines()
nerd_file = open("nerd_names.txt")
print(nerd_file.readlines())
nerd_file.close()

# Example 4 - Read the first line of a file
nerd_file = open("nerd_names.txt")
print(nerd_file.readline())
nerd_file.close()

# Example 5 - Read the first two lines
nerd_file = open("nerd_names.txt")
print(nerd_file.readline())
print(nerd_file.readline())
nerd_file.close()

# Example 6 - Read and print out hte 3rd line or item in the file
nerd_file = open("nerd_names.txt")
print(nerd_file.readlines()[2])
nerd_file.close()

# Example 7 - As is, read
nerd_file = open("nerd_names.txt")
print(nerd_file.read())
nerd_file.close()
nerd_file = open("nerd_names.txt")

# Example 8 - Read vs Readlines
# With Readlines
nerd_file = open("nerd_names.txt")
nerds = nerd_file.readlines()
nerd_file.close()

print("Example 8 - with readlines()")
print(f'Data type is: {type(nerds)}')
print(nerds)

for name in nerds:
    name = name.rstrip() + " is a Nerd."
    print(name)
print("----Readlines() Example Done----")

# With Read
nerd_file_read = open("nerd_names.txt")
nerds_read = nerd_file_read.read()
nerd_file_read.close()

print("Example 8 - with read()")
print(f'Data type is: {type(nerds_read)}')
print(nerds_read)

for name in nerds_read:
    name = name.rstrip() + " is a Nerd."
    print(name)
print("----read() Example Done----")