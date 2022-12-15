#Challenge 1
#Ask the user for their name and age, assign theses values to two variables, and then print them.

name = input("What is your name? ")
age = input ("What is your age? ")

print ("Your name is " + name)
print ("Your age is " + str(age))


#Challenge 2
#Investigate what happens when you try to assign a value to a variable that you've already defined. Try printing the variable before and after you reuse the name.

x = 5
print(x)

x = 7
#Will print 5 since 7 goes on line after print.

#Challenge 3
#fix the issues in the code

hourly_wage = input("Please enter your hourly wage: ')

prnt("Hourly wage: ")
print(hourlywage)
print("Hours worked: ")
print(hours_worked)

hours_worked = input("How many hours did you work this week? ")

#solution
hourly_wage = input("Please enter your hourly wage: ")
hours_worked = input("How many hours did you work this week? ")

print("Hourly wage: ")
print(hourly_wage)
print("Hours worked: ")
print(hours_worked)