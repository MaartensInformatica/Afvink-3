vege = input('Are you vegetarian?: ')
vega = input('Are you vegan?: ')
glut = input('Are you glutenfree?: ')

if vege and vega and glut == 'yes':
    print('Possible restaurants: ')
    print('Corner Cafe')
    print('The Chefs kitchen')
elif vege and vega == 'yes' and glut == 'no':
    print('Possible restaurants: ')
    print('Corner Cafe')
    print('The Chefs kitchen')
elif vega and glut == 'no' and vege == 'yes':
    print('Possible restaurants: ')
    print('Main street pizza company')
    print('Corner cafe')
    print('Mamas fine italian')
    print('The chefs kitchen')
elif vege and vega == 'no' and glut == 'yes':
    print('Possible restaurants: ')
    print('Main street pizza company')
    print('Corner cafe')
    print('The chefs kitchen')
elif vege and vega and glut == 'no':
    print('Possible restaurants: ')
    print('Joes gourmet burgers')
    print('Main street pizza company')
    print('Corner cafe')
    print('Mamas fine italian')
    print('The chefs kitchen')
