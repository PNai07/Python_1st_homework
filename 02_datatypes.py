# Data Types
# Computers are stupid
#They doi not understand context, and we need to be specific with data types.

#Strings
# List of Characters bundled together in a specific order
#Using Index

# print('hello')
# print(type('hello'))
#
# #Concatenation of Strings - joining of two strings
#
# string_a = 'hello there'
# name_person = 'Juan Pier'
#
# print (string_a + ' ' + name_person)
#
# #Useful methods
# #Length
# print (len(string_a))
# print (len(name_person))
#
# #Strip = Removes trailing white spaces
#
# string_num = ' 90323 '
# print(type(string_num))
# print(string_num)
# print(string_num.strip())
#
# #.split - a method for strings
# #It splits in a specific location and output a list (data type)
#
# string_text = 'Hello I need to go to the loo'
# split_string =string_text.split(' ')
# print(split_string)
#
# #Capturing User Input -  capture and display user input
#
# #user_input_first_name = input('What is your first name')
# #print (user_input_first_name)
#
# # get user input and print first and last name
# # 1) get user input/ first name
# # save user input to variable
# first_name = input ('What is your first name')
# # get user last name
# # and save it to variable
# last_name  = input ('what is your last name?')
#
# #user_input_last_name = input('What is your last name')
# #print (user_input_last_name)
#
#
# # join two and
# # Let us use concactenation
# # Let us use interpolation
# # print

# full_name = first_name +' ' +last_name
# print (full_name)
# #Let us use interpolation
# welcome_message  = f"Hi {full_name} you are very welcome!"
# print(welcome_message)

# Count /lower/ upper/ capitalize
text_example = "Here is some text, with lot's of text"
#Count
print(text_example.count('e'))
print(text_example.count('text'))

#lower
print(text_example.lower())

#Upper
print(text_example.upper())

#Capitalize
print(text_example.capitalize())
print('PIZZAHUT'.strip().capitalize())
print('PizzaHut'.capitalize())
print('pizza hut'.capitalize())
