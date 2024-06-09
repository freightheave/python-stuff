# Create a program that asks the user for a number and 
# then prints out a list of all the divisors of that number.

ansList = []
i = 1

dividend = int(input("Number? "))

#computation speed falls apart for large numbers
while i <= dividend:
    if dividend % i == 0:
        ansList.append(i)
    i+=1 

print("Divisor list is -", end = " ")
print(ansList)
