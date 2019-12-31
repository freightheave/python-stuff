#executing the XOR gate

print('Enter a truth value for each of the variables and get A XOR B.')

print('Enter A')

a = input()

print('Enter B')

b = input()

print('The XOR gate value is:')

print(((a and (not b)) or ((not a) and b)))

