# Improved writing and reading

# Example 1 
with open('some_file.txt', 'w') as writer:
    writer.write('Hey I wrote using the `with` keyword :]')

with open('some_file.txt', 'r') as reader:
    read_data = reader.read()

print(read_data)

# Example 2 - But wait! We didn't close the file!?
print(f'Did we close the reader file? {reader.closed}')
print(f'Did we close the writer file? {writer.closed}')






