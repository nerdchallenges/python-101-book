# Example - Escapes

print("Casey says \"Welcome to the Nerd Challenges Python 101 Course\"")

# Example - Concatenation
print("Hello " + "Casey" + " Welcome to Nerd Challenges Python 101 Course!")
nerd_name = "Casey"
print("Hello " + nerd_name + " welcome to Nerd Challenges Python 101 Course")

# Example - String Formatting
book_chapter = 2
python_series = 101
age = 34
programming_experience = 0
statement = "We are on Chapter {} of the Python {} book. I am {} with {} python experience."
print(statement.format(book_chapter, python_series, age, programming_experience))

# Example - Legacy Operator
company_name = "Nerd Challenges LLC."
print("Hello %s" % company_name) 

# Example - Modifier, integer
nerd_age = 34.5
print("This user is %i" % nerd_age)

# Example - Modifier, string and integer
company_name = "Nerd Challenges"
nerd_age = 34.5
print("Hey Casey is from %s and currently %i years old" % (company_name, nerd_age))
print("Hey Casey is from %(company_name)s and currently %(nerd_age)i years old" % {"company_name": "Nerd Challenges LLC", "nerd_age": 34.5})

# Example - fStrings
book_chapter = 1
python_series = 101
print(f"We are on Day {book_chapter} of the Python {python_series} book.")

book_chapter = 1
python_series = 101
print(f"We are on Day {book_chapter + 1} of the Python {python_series} book.")