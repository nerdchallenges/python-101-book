# Writing files with Python is fun :D

# Example 1 - Write Mode
# Creates a new file
vowels_file = open("vowels_list.txt" ,"w")

# Create a list of vowels and write that list as a string to the new text file.
vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_file.write(f'This is a list of all the vowels: {vowels_list}')

vowels_file = open("vowels_list.txt", "r")
print(vowels_file.read())

vowels_file.close()

# Example 2 - Write vs Append Mode
# Creates a new file
vowels_file = open("vowels_list.txt" ,"w")

# Create a list of vowels and write that list as a string to the new text file.
vowels_list = ['a', 'e', 'i', 'o', 'u']
vowels_file.write(f'This is a list of all the CONSTANTS: {vowels_list}')

vowels_file = open("vowels_list.txt", "r")
print(vowels_file.read())

vowels_file.close()

# Example 3 - Create a file
new_file = open("created_file.txt", "x")
new_file.close()

# Example 4 - Delete a file
import os
os.remove("created_file.txt")

# Example 5 - Removing a directory
os.rmdir('testDirectory')
print("The directory has been deleted!")
