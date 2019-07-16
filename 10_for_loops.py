# For loops in Python
# used to iterate over collections. list and dictionaries
#placeholder in a variable that it's scope is limited to loop or function

# SYNTAX
# for <placeholder> in <list>:
 # run block of code
 # In this example - the word 'landlords' can be the placeholder


# x_crazy_landlords = ['Cruella de Ville', 'Donald Duck', 'Popeye the Maltese']
# print('starting loop')
# counter = 0
# time.sleep(1)
# for land_l in x_crazy_landlords:
#     print('hello')
#     print(land_l)
#     print(counter)
#     counter += 1
#     time.sleep(3)
# print('loop ended')
#     # loop goes through the array and displays hello, 'landlord'
#
# x_crazy_landlords = ['Cruella de Ville', 'Donald Duck', 'Popeye the Maltese']
# counter  = 1
# for land_lord in x_crazy_landlords:
#     print(counter, '-', land_lord)
#     counter += 1

## Further loops
import time
list_data = [1, 2, 3, 4, 5]
embedded_list = [[1, 2, 3],[5, 6, 7]]

# for num in list_data:
#     print(num)

# for data in embedded_list:
#     print(data)
#     data_set = [1, 2, 3]
# for num in data:
#     print(num)
#     time.sleep(1)

# # Class Exercise Spartans
# list_names= ['payal', 'michael', 'omid', 'naila', 'dan', 'ally', 'matt', 'zaid', 'pratheep', 'shavgath']
# for name in list_names:
#     print('hello', name) # for <placeholder> in <list>
#

# list_scores = [1, 10, 3, 4, 5, 6]
#
# for num in list_scores:
#     result_percent = num / 10 * 100
#     print(result_percent)


list_embed_scores= [[10, 5, 2],[3, 4, 6]]
for ind_list in list_embed_scores:
     print(ind_list)

for num in ind_list:
    print (num*2)