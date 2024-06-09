# write a program that prints out all the elements of the 
# list that are less than input and write it in one line.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#sol 1 & 2
print( [ i for i in a if i < 5 ] )

#sol 3
checkNum = float(input("Num check vs?: "))
print( [ i for i in a if i < checkNum ] )
