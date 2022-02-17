# Example 1 - Lists
geek_names = ["Nikola", "Tesla", 100, "Thomas", "Edison"]
print(geek_names)

# Example 2 - Index lists
geek_names = ["Nikola", "Tesla", 100, "Thomas", "Edison"]
print(geek_names[3])
print(geek_names[-1])
print(len(geek_names))
print(geek_names[0:4])
print(geek_names[0:])
print(geek_names[1:4])

# Example 3 - Adding to a list
geek_names = ["Nikola", "Tesla", 100, "Thomas", "Edison"]
geek_names[2] = "Einstein" 
print(geek_names)

# Example 4 - Getting an index
geek_names = ["Nikola", "Tesla", 100, "Thomas", "Edison"]
print(geek_names.index("Tesla"))

# Example 5 - Lists
nerd_names = ["CJ", "Albert" , "Kelv", "Prodigy", "Rico", "Jamison"]
geek_names = ["Nikola", "Tesla", "Thomas", "Edison"]
nerd_ages = [8, 12, 25, 13, 15, 18]
geek_ages = [1, 16, 14, 22, 10, 31]
nerd_pop = ["pop1", "pop2", "pop3"]

# Example 6 - Tuples
my_shapes = ("Circle", "Rectangle", "Triangle", "Square")
my_shapes[1] = "Trapezoid"
print(my_shapes)

my_shapes = ("Circle", "Rectangle", "Triangle", "Square", [0, 4, 4, 3])
print(my_shapes)

# Example 7 - Sets
my_die = {1, 2, 3, 4, 5, 6, 1, 2}
print(my_die)
print(3 in my_die)

# Example 8 - Set Functions
my_vowels = {"a", "e", "i", "o", "u"}
my_alpha = {"a", "b", "c", "d", "e"}
print(my_vowels.intersection(my_alpha))
print(my_vowels.difference(my_alpha))
print(my_vowels.union(my_alpha))

# Example 9 - Dictionaries
day_conversion = {
    "Mon": "Monday",
    "Tues": "Tuesday",
    "Wed": "Wednesday",
    "Thurs": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
 }

print(day_conversion)
print(day_conversion["Wed"])
print(day_conversion.get("not_in_dictionary"))
day_conversion["Sun"] = "Funday"
print(day_conversion)

# Example 10 - Dictionary with objects
caseydict = {
    "name": {
        "prefix": "Mr.",
        "first": "Casey",
        "last": "Gerena",
        "suffix": "Jr"
    },
    "job": {
        "company": "Nerd Challenges LLC",
        "position": "Lead Nerd",
        "location": {
            "address": "123 NC Blvd",
            "city": "Tampa",
            "state": "Florida",
            "zip": 33601
        }
    }
}
print(caseydict)

# Example 11 - Implicit Type Conversion
nerd_name = "Casey"
nerd_age = 34
pi = 3.1415926535897

nerd_names = ["CJ", "Albert", "Kelv", "Prodigy", "Rico", "Jamison"]
my_shapes = ("Circle", "Rectangle", "Triangle", "Square")
my_die = {1, 2, 3, 4, 5, 6, 1, 2}

print(type(nerd_name))
print(type(nerd_age))
print(type(pi))
print("\n")
print(type(nerd_names))
print(type(my_shapes))
print(type(my_die))

# Example 12 - Dictionary Type Conversion, implicit
day_conversion = {
    "Mon": "Monday",
    "Tues": "Tuesday",
    "Wed": "Wednesday",
    "Thurs": "Thursday",
    "Fri": "Friday",
    "Sat": "Saturday",
    "Sun": "Sunday",
}
print(type(day_conversion))

# Example 13 - More Implicit conversion
nerd_age = 34
pi = 3.1415926535897
sum = nerd_age + pi
print(sum)
print(type(sum))

# Example 14 - Explicit conversion
nerd_name = "Casey"
nerd_age = 34
print(nerd_name + " is of the age " + str(nerd_age))