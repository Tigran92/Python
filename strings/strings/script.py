# They're all Lists!
my_name = "Marco"

first_initial = my_name[0]
print(first_initial)


# Cut Me a Slice of String
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]

temp_password = last_name[2:6]

print(new_account)
print(temp_password)


# Concatenating Strings
first_name = "Julie"
last_name = "Blevins"

def account_generator(first_name, last_name):

  return first_name[:3] + last_name[:3]

new_account = account_generator(first_name, last_name)

print(new_account)


# More and More String Slicing (How Long is that String?)
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):

  len(first_name)
  len(last_name)

  return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]

temp_password = password_generator(first_name, last_name)

print(temp_password)


# Negative Indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

print(second_to_last)
print(final_word)


# Strings are Immutable
first_name = "Bob"
last_name = "Daily"
fixed_first_name = "R" + first_name[1:]

print(fixed_first_name)


# Escape Characters
password = "theycallme\"crazy\"91"
print(password)


# Iterating through Strings
def get_length(string):

  count = 0

  for i in string:

    count += 1
  return count
print(get_length("COUNTING"))


# Strings and Conditionals (Part One)
def letter_check(word, letter):

  for i in word:

    if i == letter:

      return True

  return False

print(letter_check("remember", "e"))


# Strings and Conditionals (Part Two)
def contains(big_string, little_string):

 if (little_string in big_string):

   return True
 else:
   return False

print(contains("watermelon", "melon"))

def common_letters(string_one, string_two):

  letters = []

  for i in string_one:

    if i in string_two and not i in letters:

      letters.append(i)
  return letters


print(common_letters("hello", "hola"))

# Username and Password Generators
def username_generator(first_name, last_name):

  if(len(first_name) >= 3) and (len(last_name) >= 4):

    username = first_name[:3] + last_name[:4]
  else:
    username = first_name + last_name

  return username


user_name = username_generator("Abe", "Simpson")
print(user_name)

def password_generator(user_name):

    password = ""

    for i in range(0, len(user_name)):

        password += user_name[i-1]

    return password

print(password_generator(user_name))
