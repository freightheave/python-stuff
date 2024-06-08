#executing the XOR gate

print('Enter a truth value for each of the variables and get A XOR B.')

print('Enter A')

a = False

print('Enter B')

b = True

print('The XOR gate value is:')

print(((a and (not b)) or ((not a) and b)))


'''
A 	B 	A XOR B
0 	0 	0
0 	1 	1
1 	0 	1
1 	1 	0 
'''