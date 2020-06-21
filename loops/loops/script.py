# Create a For Loop
board_games = ['Settlers of Catan', 'Carcassone', 'Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American', 'hockey', 'baseball', 'cricket']

for game in board_games:
  print(game)

for sport in sport_games:
  print(sport)


  # Using Range in Loops
promise = "I will not chew gum in class"

for i in range(5):
  print(promise)


  # Infinite Loops
students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  students_period_B.append(student)
  print(student)


 # Break
dog_breeds_available_for_adoption = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
  print(breed)
  if(breed == dog_breed_I_want):
    print("They have the dog I want!")
    break


# Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for i in ages:
  if (i < 21):
    continue
  print(i)


  # While Loops
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while (len(students_in_poetry) < 6):

  students_in_poetry.append(all_students.pop())

print(students_in_poetry)


# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for i in location:
    scoops_sold += i

print(scoops_sold)


# List Comprehensions
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [height for height in heights if height > 161]

print(can_ride_coaster)


# More List Comprehensions
celsius = [0, 10, 15, 32, -5, 27, 3]

fahrenheit = [in_celsius * 9/5 + 32 for in_celsius in celsius]

print(fahrenheit)


single_digits = range(10)
squares = []

for i in single_digits:
  print(i)
  squares.append(i**2)

print(squares)


cubes = [cube ** 3 for cube in single_digits]

print(cubes)
