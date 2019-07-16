# # List and Dictionaries
# # List
#
# #Sometimes we need to list our crazy pokemons
# # Because we don't want to work there
#
#
# # This is how you make a list
# # [] seperate items using,
# # ['bananas', 'pine', 'gasoline']
# # declaring a list and saving to variable
# crazy_pokemons = [' Snorlax', 'Jigglipuff', 'Mewtoo']
# print(crazy_pokemons)
# print(type(crazy_pokemons))
#
# # Lists are organised using index
# # [ 0    , 1     ,  2]
# # [ 3    , 2,    ,  1]
# # ['bananas', 'pine', 'gasoline']
# # Indexes start at 0
#
#
# print (len(crazy_pokemons))
# print (crazy_pokemons [2])
# print (crazy_pokemons [0])
#
# # if you want to print the last in the list
# # you have two options
# # array[len(array) -1]
#
# print(crazy_pokemons[len(crazy_pokemons)-1])
# print(crazy_pokemons[-1])
#
# # Re-Assigning a value in a list, using a index
# # We need to evolve Mewtoo to Mewtree
#
# print(crazy_pokemons)
# crazy_pokemons[2] = 'Mewtree'
# print(crazy_pokemons)
#
# #Appending a new pokemon
# #We caught a pigeoto
# crazy_pokemons.append('Pigeoto')
# print (crazy_pokemons)
#
# crazy_pokemons.insert(3, 'Rattata')
# print(crazy_pokemons)
#
# #Removing a record
# crazy_pokemons.pop()
# print(crazy_pokemons)
# crazy_pokemons.pop(0)
# print(crazy_pokemons)
#
# #Removing using a filter
# crazy_pokemons.remove('Rattata')
# print(crazy_pokemons)
#
# #Lists can have any datatypes
# mixed_list = ['Jones', 10, 42, 'John']
# print (mixed_list)
# print (type(mixed_list[0]), type(mixed_list[1]))
#
#
#
# #Inception List
# leo_d = ['first', 2, ['leo', 'd']]
# print('accessing the index 2')
# print(leo_d[2])
# print(leo_d[2][1])
# sub_array = leo_d[2]
# print(sub_array)
# print(sub_array[1])
#
# #All of this is the same as
# print (leo_d[2][1])


#  TUPLES
# Tuples are immutable lists
# Meaning they do not change #
# Syntax -
# tuple_list  = ('hello', 10, 13, 4)

my_tuple = ('eggs', 'bread', 'oats', [11, 13])
print(my_tuple)
print(type(my_tuple))

# We cannot change the tuple itself, but we can change the state of items inside
# we cannot re-assign them.
breakpoint()

