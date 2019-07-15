#Dictionaries AKA Hashes

# Work with key:  value pairs. As opposes

#Declaring a Hash/ dictionary
pika = {}


# Dictionaries work with keys: values
pika ={'name': 'Derik',
'pokemon' : 'Pikachu',
'age': 17,
'personality': 'Grumpy'
}

print(pika)
print(type(pika))

# Access information using keys
print(pika['age'])
print(pika['pokemon'])

# Re assign values, using the key
pika['age'] = 18
print(pika['age'])

#adding a key : value pair
pika['colour'] = 'Yellowish'
print(pika)

#Creating key : value for first & last name
full_name = pika['name'].split()
print(full_name)
first_name = full_name[0]
print(first_name)
pika['first_name'] = first_name
pika['last_name'] = full_name[1]
print(pika)

#Embedded Data
pika ={'name': 'Derik',
'pokemon' : 'Pikachu',
'age': 17,
'personality': ['grumpy','jumpy','shocking', 'static']
       }
print(pika('personality'))


#Important methods
keys = pika.keys()
print(keys)

values = pika.values()
print(values)

pika.values(keys[1])