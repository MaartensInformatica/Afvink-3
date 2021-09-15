#Maak een variabele aan en vraag om een float
pocket = float(input('insert pocket number: '))

#We zoeken naar een getal tussen twee marges en of het even of oneven is. Daarom gebruiken we '> and < and %2'. 
#Als de eerste niet waar is gaan we naar de volgende. Dus if, elif, elif etc... totdat alle ifs onwaar zijn. In dat geval is de invoer buiten de marge. Dan gebruiken we else.
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
    
    
