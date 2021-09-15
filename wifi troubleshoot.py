#In beginsel werkt de wifi niet dus starten we met de eerste stap
print('reboot the computer and try to connect')

#Vraag of de eerste stap geholpen heeft
answer = input('did that fix the problem?: ')

#Iedere keer dat er nee geantwoord wordt, printen we een nieuwe vraag. Daarom if, if, if etc..
if answer == 'no':
    print('reboot the router and try to connect')
    answer2 = input('did that fix the problem?: ')
    if answer2 == 'no':
        print('make sure the cables between the router & modem are plugged in firmly')
        answer3 = input('did that fix the problem?: ')
        if answer3 == 'no':
            print('move the router to a new location and try to connect')
            answer4 = input('did that fix the problem?: ')
            if answer4 == 'no':
                print('get a new router')
if answer or answer2 or answer3 or answer4 == 'yes':
    print('doei')
#De code waarbij ja als antwoord wordt gegeven moet op bij elke vraag van toepassing zijn. 
#Daarom staat deze op hetzelfde niveau als de eerste vraag maar heeft het wel alle anwtwoordmomenten als variabelen  
    
