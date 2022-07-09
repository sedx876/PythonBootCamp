import random
import my_module
# Randomisation and Python List

random_integer = random.randint(1, 100)
print(random_integer)

random_float = random.random() * 5
print(random_float)

print(my_module.pi)

random_side = random.randint(0, 1)
if random_side == 1:
    print('HEADS')
else:
    print('TAILS')

# LISTS-Data Structure Known as an Array in other coding languages

usa = ['Delaware', 'Pennsylvania', 'New York']
usa.append('Anarchy')
print(usa)
print(usa[2])

names = ['Sharon', 'Mike', 'Andy', 'Leaf', 'Austin', 'Rys']
num_items = len(names)
ran_choice = random.randint(0, num_items - 1)
person = names[ran_choice]
print(person)