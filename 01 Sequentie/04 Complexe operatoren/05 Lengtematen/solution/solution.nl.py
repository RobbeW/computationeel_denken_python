# Invoer
lengte = float( input('Geef een lengte in (in m): '))

# Verwerking
lengte_in_inch = lengte * 100 / 2.54

aantal_yard = int(lengte_in_inch // 36)
rest_yard = lengte_in_inch % 36

aantal_feet = int( rest_yard // 12)
rest_feet = rest_yard % 12

aantal_inch = round(rest_feet, 2)

# Uitvoer
print('Dit stemt overeen met', aantal_yard, 'yard', aantal_feet, 'feet', aantal_inch, 'inch')
