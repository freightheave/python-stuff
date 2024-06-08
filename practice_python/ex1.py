import datetime

#inputs are always strings.
name = input("What's your name?   ")
age = input("What's your age?   ")

now = datetime.datetime.now()

print(name + " you will turn 100 years old in the year: " + str(now.year - int(age) + 100))