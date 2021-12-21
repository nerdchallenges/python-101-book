# If Else Part 2
# Theme Park Examples

# Example 1
rider_age = 20
age_limit = 16
tall = True

if rider_age >= age_limit and tall:
    print("Congrats! You are old enough and tall enough for this ride.")
elif rider_age >= 13 and tall:
    print("You are almost old enough to go on this ride, but you are tall enough!")
else:
    print("Sorry, you are way too young or way too short to go on this ride!")

# Example 2
rider_age = 10
age_limit = 16
tall = False

if rider_age >= age_limit or tall:
    print("Congrats! You are old enough or tall enough for this ride.")
else:
    print("Sorry, you are way too young or way too short to go on this ride!")
