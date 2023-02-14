'''
lec4
dict and tupole
'''

my_tuple = ('a','b','c','d','e')

#my_tuple[0]='f'
print(my_tuple[-1])

my_car = { 
         'color':'pink', 
         'maker': 'toyota', 
         'year': 2015 
         }
print(my_car.get('color'))
print(my_car['color'])
my_car ['model'] = 'venza'
print(my_car)
my_car['year'] = 2020
print(my_car)

print(len(my_car))
print('color'in my_car)


