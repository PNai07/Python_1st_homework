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
    print('Take an umbrella and a jacket!!')

elif weather == 'rainy':
    print('Today is a rainy day, take an umbrella!')

else:
    print ('have a great day! :)')