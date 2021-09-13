pocket = float(input('insert pocket number: '))

if pocket > 0 and pocket < 11 and pocket %2 == 1:
    print('red')
elif pocket > 0 and pocket < 11 and pocket %2 == 0:
    print('black')
elif pocket > 10 and pocket < 19 and pocket %2 == 1:
    print('black')
elif pocket > 10 and pocket < 19 and pocket %2 == 0:
    print('red')
elif pocket > 18 and pocket < 29 and pocket %2 == 1:
    print('red')
elif pocket > 18 and pocket < 29 and pocket %2 == 0:
    print('black')
elif pocket > 28 and pocket < 37 and pocket %2 == 1:
    print('black')
elif pocket > 28 and pocket < 37 and pocket %2 == 0:
    print('red')
elif pocket == 0:
    print('green')
else:
    print('error: pocketnumber outside of range')
    
    
