# Sum Values
def sum_values(my_dictionary):

  sum_of_values = 0
  for keys in my_dictionary:

    sum_of_values += my_dictionary[keys]
  return sum_of_values

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6


# Even Keys
def sum_even_keys(my_dictionary):

  sum_of_even_keys = 0
  for keys in my_dictionary:

    if keys % 2 == 0:
      sum_of_even_keys += my_dictionary[keys]
  return sum_of_even_keys

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6


# Add Ten
def add_ten(my_dictionary):

  for keys in my_dictionary:

    my_dictionary[keys] += 10

  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
