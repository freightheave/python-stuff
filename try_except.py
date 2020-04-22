def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        return(print('Error: WTF You can\'t divide by zero, you moron!'))

i=0
while i<=5:
    print(div42by(i))
    i+=1
