# Booleans

# Booleans are a data type that is either TRUE or FALSE

var_true = True
var_false = False

#Syntax is capital letter

print(type(var_true))
print(type(var_false))

# When we equate/ evaluate something we get a boolean as a response.
# Logical operator return boolean
# == / ! / <> / >= / <=

weather = 'Rainy'
print(weather =='Sunny')
print (weather== 'Rainy')

#Logical **AND** & ** OR **
# evaluate two sides, BOTH have to be true for it to return True
print ('<Testing logical and: ')
print(weather== 'Rainy') and (weather== 'Sunny')
print(True and False)
#True

print ('<Testing logical and: ')
print(weather== 'Rainy') and (weather== 'Rainy')
print(True and True)

#Logical OR - One of the side




# Some methods or functions can return booleans
potential_number = '10'
print('hey')
print(potential_number.isnumeric())
print(potential_number.isinteger())

print ('location in code!')
print (potential_number.isnumeric())

print ('Location in code 2')
text = 'Hello World'
print(text[0] =='H')
print(text.startswith('h'))
print(text.startswith('H'))
print ('Testing. endswith.(arg)')
print (text[-1]== '!') # Strings are list of characters. -1 represents the last index in said list
print(text.endswith('!'))
print(text.endswith('?'))


#Booleans and Numbere

print("printing bool values of numbers")
print (bool(13))
print (bool(-1))
print (bool(3.14))
print (bool(1+3j))

#Value of None
print (bool(None))
