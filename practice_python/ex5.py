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

# generate random list lengths
randList1Len = int(random.randint(1,50))
randList2Len = int(random.randint(1,50))

# generate 2 random lists & init the final answer list
randList1 = randListGen(randList1Len)
randList2 = randListGen(randList2Len)

# find the common elements & sort the resulting list
comElemList = list(set(randList1) & set(randList2))
list.sort(comElemList)

# printing...
print("First generated array - ")
print(randList1)
print("Second generated array - ")
print(randList2)      
print("List of common elements - ")
print(comElemList)

# ------------------------------- Deprecated Inefficient code --------------------------

# import random

# random list generator
# def randListGen(listLen):
#     return [random.randint(1, 100) for _ in range(listLen)]
# this is insane! you can just do: 
# return [<expression>]/{<expression>}/(<expression>) and return a list/set/tuple!
#
# for _ in range(x): -> Don't care iterator value, just run loop for range(x) times.
#
# randList1Len = int(random.randint(1,50))
# randList2Len = int(random.randint(1,50))
#
# generate 2 random lists & init the final answer list
# randList1 = randListGen(randList1Len)
# randList2 = randListGen(randList2Len)
# tempList = []
# comElemList = []
#
# def bubSort(listArg):
#     for i in range(len(listArg)):
#         swapped = False #initialise to false as no swaps have happened
#         for j in range(0, len(listArg)-i-1): #-1 because array indices start from 0
#             if listArg[j] > listArg[j+1]:
#                 (listArg[j], listArg[j+1]) = (listArg[j+1], listArg[j]) 
#                 #just swap if i+1 < i
#                 swapped = True 
#         if swapped == False:
#             #if control comes out of J loop with swapped = false, 
#             # it means all swaps have happened.
#             break    
#
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
# DEBUG: print("len of com elems is " + str(len(comElemList)))
# 
# remove duplicates
# for i in reversed(range(len(tempList))): # reversed(range()) is iterating backwards
#     if tempList[i-1] == tempList[i]:
#         comElemList.append(tempList[i])
# 
# bubSort(comElemList)
#
# print("First generated array - ")
# print(randList1)
# print("Second generated array - ")
# print(randList2)      
# print("List of common elements - ")
# print(comElemList)
#