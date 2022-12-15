#Challenge 1
#Using the variable below, print "Hello, world!".

greeting = "Hello, world"

#solution

greeting1 = "Hello, world"
greeting2 = "Hello, world{}"

print(f"{greeting1}!")
print(greeting2.format("!"))

#Challenge 2
#Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.

name = input("What is your name? ").strip().title()

print (f"Hello, {name}!")

#Challenge 3
#Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".

name = "I am "
number = 29

print(name + str(number))

#Challenge 4
#Format and print the information below using string interpolation:

title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}), directed by {director}")