#maak een integere variabele van de userinput
number = int(input('insert an integer: '))

#gebruik if en print de string positief voor getallen hoger dan 0 en een elif met de print negatief voor getalen lager dan 0 
if number > 0:
    print('positief')
    
elif number < 0:
    print('negatief')
#is het noch positief noch negatief, dan is de enige andere uitkomst 0 dus daar hoef je niet eens een elif voor te gebruiken, gewoon else: print zero
else:
    print('zero')
#boolian voor percentageberekening
if number %2 == 1 :
    print('odd')
#is het niet oneven? dan moet het wel even zijn, else: print even
else:
    print('even')
    
