# Write a program that returns a list that contains only the elements 
# that are common between the lists (without duplicates). Common numbers only.
# Make sure your program works on two lists of different sizes.

import random

# random list generator
def randListGen(listLen):
    return [random.randint(1, 100) for _ in range(listLen)]
# this is insane! you can just do: 
# return [<expression>]/{<expression>}/(<expression>) and return a list/set/tuple!

# for _ in range(x): -> Don't care iterator value, just run loop for range(x) times.

randList1Len = int(random.randint(1,50))
randList2Len = int(random.randint(1,50))

randList1 = randListGen(randList1Len)
randList2 = randListGen(randList2Len)
tempList = []
comElemList = []

# TODO: Avoid nested loops & duplicate matches. Ans - Just use sets! 
# (But sets cannot be called with set[i])...
# ONE LINER SOL: answerList = list(set(a) & set(b))
# if randList1Len > randList2Len:
#     for i in range(randList1Len):
#         for j in range(randList2Len):
#             if randList1[i] == randList2[j]:
#                 tempList.append(randList1[i])
# else:
#     for i in range(randList2Len):
#         for j in range(randList1Len):
#             if randList1[j] == randList2[i]:
#                 tempList.append(randList2[i])
# 
# bubSort(tempList)
# 
# # DEBUG: print("len of com elems is " + str(len(comElemList)))
# 
# # remove duplicates
# for i in reversed(range(len(tempList))): # reversed(range()) is iterating backwards
#     if tempList[i-1] == tempList[i]:
#         comElemList.append(tempList[i])
# 
# bubSort(comElemList)

comElemList = list(set(randList1) & set(randList2))
list.sort(comElemList)

print("First generated array - ")
print(randList1)
print("Second generated array - ")
print(randList2)      
print("List of common elements - ")
print(comElemList)
