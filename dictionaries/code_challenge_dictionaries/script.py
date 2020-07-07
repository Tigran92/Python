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


# Values That Are Keys
def values_that_are_keys(my_dictionary):

  new_values_list = []
  for values in my_dictionary.values():

    if values in my_dictionary.keys():

      new_values_list.append(values)
  return new_values_list


print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]


# Largest Value
def max_key(my_dictionary):

  largest_key = float("-inf")
  largest_value = float("-inf")
  for keys, values in my_dictionary.items():

    if values > largest_value:

      largest_value = values
      largest_key = keys

  return largest_key


print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"


# Word Length Dict
def word_length_dictionary(words):

  new_dictionary = {}
  for word in words:

    new_dictionary[word] = len(word)

  return new_dictionary


print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}


# Unique Value
def unique_values(my_dictionary):

  unique_values = []
  unique_values_count = 0
  for values in my_dictionary.values():

    if values not in unique_values:

      unique_values.append(values)
      unique_values_count += 1
    else:
      continue
  print("Unique Value's List: " + str(unique_values))
  return unique_values_count



print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1


# Count First Letter
def count_first_letter(names):

  new_dictionary = {}
  for keys in names:

    first_letter = keys[0]
    if first_letter not in new_dictionary:

      new_dictionary[first_letter] = 0

    else:
      new_dictionary[first_letter] += len(names[keys])

  return new_dictionary


print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
