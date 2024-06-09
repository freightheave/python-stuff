import random

# declaratives
list = []
randLen = int(random.random() * 100)

# generate random list of random len
for i in range(randLen):
    list.append(float(random.random() * 10))

print(f"list of {randLen} has been created. Now sorting...")
print(list)

# bubble sort, oof
# swap if a < b but when to stop?
# if len = n, then you need n runs of n runs each. 
# i = 1 subloops from j = 0 to n-1: checks, compares & swaps ... till,
# i = n subloops from j = 0 to n-1: checks, compares & swaps.
# O(n^2)

def bubSort(listArg):
    for i in range(len(listArg)):
        swapped = False #initialise to false as no swaps have happened
        for j in range(0, len(listArg)-i-1): #-1 because array indices start from 0
            if listArg[j] > listArg[j+1]:
                (listArg[j], listArg[j+1]) = (listArg[j+1], listArg[j]) 
                #just swap if i+1 < i
                swapped = True 
        if swapped == False:
            #if control comes out of J loop with swapped = false, 
            # it means all swaps have happened.
            break    

bubSort(list)
print("sorted list is -")
print(list)