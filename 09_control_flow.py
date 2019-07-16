# Control Flows - IF Statements
# syntax - INDENTATION MATTERS
# if<condition>:
#else:
 # Block of Code




# age = 70
#
# if age >18:
#      print('your age is above 18, you can vote and go to prison')
#
# elif age >=70:
#     print('you can do everything, just take it easy')
#
# elif age >= 16:
#     print('you can buy a lottery ticket and probably go to prison, but records will be kept for a while')
#
# else:
#     print('you are too young to do anything')



weather = input("What is the weather like?").lower().strip()

if weather =='rainy' or weather == 'stormy' :
    print('You will need a jacket!!')
elif 'rainy' in weather:  #allows to search for 'rainy' within a string e.g. dkgg rainy etc
    print('You will need your umbrella!')
elif weather == 'sunny':
    print('Take your sunglasses and pop on some sunscreen!')
elif weather =='foggy':
    print('You may need an umbrella, because you never know!')
else:
    print ('have a great day! :)')

# #I want a jacket when it is rainy and stormy
# I want a umbrella when it is rainy
# I also want a umbrella if it is foggy, because you never know
# keep stuff from sunny