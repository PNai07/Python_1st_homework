# Our Bread Factory



def make_dough(ingredient1, ingredient2):
   if 'wheat' in ingredient1 and 'water'in ingredient2:
       return 'dough'

def bake_bread(semi_product):
    return 'bread'
else:
return 'wrong ingredients'

def bake_bread (semi_product):
    if semi_product == 'dough':
        return 'bread'
    else: return ' wrong ingredients'

print(make_dough('wheat', 'water'))
print(make_dough('cement', 'water'))


# Tests
print ('call function to make_dough, expect dough to be returned')
print (make_dough('wheat','water') == 'dough')

print ('call function to bake_bread, expect bread to be returned')
print (bake_bread ('dough') == 'bread')