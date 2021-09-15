#maak 4 variabelen aan voor de 4 afmetingen en laat de gebruiker deze invoeren
lengte1 = input('lengte eerste rechthoek: ')
breedte1 = input('breedte eerste rechthoek: ')
lengte2 = input('lengte tweede rechthoek: ')
breedte2 = input('breedte tweede rechthoek: ')

#bereken de oppervlaktes
oppervlakte1 = float(lengte1)*float(breedte1)
oppervlakte2 = float(lengte2)*float(breedte2)

#gebruik if als rechthoek 1 groter is, elif als dat niet waar is en rechthoek 2 groter is en else als beide onwaar zijn.
if oppervlakte1 > oppervlakte2: print('rechthoek 1 is groter')
elif oppervlakte1 < oppervlakte2: print('rechthoek 2 is groter')
else: print('rechthoeken zijn even groot')




                                
