#Lists
ints_and_strings = [1, 2, 3, 'four', 'five', 'six']

sam_height = ['Sam', 67]

print(ints_and_strings)



#Lists of Lists
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]

ages = [['Aaron', 15], ['Dhruti', 16]]

print(ages)



#Zip
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

list_of_names_and_dogs_names = list(names_and_dogs_names)

print(list_of_names_and_dogs_names)



#Growing a List: Append
orders = ['daisies', 'periwinkle']

print(orders)

orders.append('tulips')
orders.append('roses')

print(orders)



#Growing a List: Plus (+)
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']

# Create new orders here:
new_orders = orders + ['lilac', 'iris']

broken_prices = [5, 3, 4, 5, 4] + [4]

print(new_orders)
print(broken_prices)



#Range I
list1 = range(9)
list2 = range(8)

print(list(list1), list(list2))



#Range II
list1 = range(5, 15, 3)

print(list(list1))

list2 = range(0, 40, 5)

print(list(list2))



first_names = ['Ainsley', 'Ben', 'Chani', 'Depak']

age = []

age.append(42)

all_ages = [32, 41, 29] + age

print(all_ages)

name_and_age = zip(first_names, all_ages)

print(list(name_and_age))

ids = range(4)

print(list(ids))
