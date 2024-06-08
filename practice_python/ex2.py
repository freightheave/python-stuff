def isEven(readVar):
    if readVar % 2 == 0:
        return 1
    else:
        return 0
    
def isDivByFour(readVarFour):
    if readVarFour % 4 == 0:
        return 1
    else:
        return 0
    
def isDiv(var1, var2):
    if var1 % var2 == 0:
        return 1
    else:
        return 0
    
divby2 = isEven(int(input("Gif number: ")))
if divby2 == 1:
    print("Div by 2 success!")
else:
    print("Odd number dumass!")

divby4 = isDivByFour(int(input("Gif number: ")))
if divby4 == 1:
    print("Div by 4 success!")
else:
    print("undivisibly by number dumass!")

divbydiv1 = int(input("Gif dividend: "))
divbydiv2 = int(input("Gif divisor: "))
divbydiv = isDiv(divbydiv1, divbydiv2)
if divbydiv == 1:
    print(f"Div success!")
else:
    print("Not div success.")
