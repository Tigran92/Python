# Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):

  count = 0
  for i in letters:

    if i in word:
      count += 1

  return count


print(unique_english_letters("WOrld"))


# Count X
def count_char_x(word, x):

  count_x = 0
  for i in word:

    if(i in x):

      count_x += 1

  return count_x

print(count_char_x("mississippi", "s"))


# Count Multi X
def count_multi_char_x(word, x):

  count_x = 0

  h = word.split(x)
  c = len(h) - 1
  count_x += c

  return count_x

print(count_multi_char_x("mississippi", "iss"))
# should print 2
print(count_multi_char_x("apple", "pp"))
# should print 1


# Substring Between

def substring_between_letters(word, start, end):

  find_start = word.find(start)
  find_end = word.find(end)

  if(find_start <= -1) or (find_end <= -1):
    return word
  else:
    return word[find_start+1:find_end]


print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"


# X Length
def x_length_words(sentence, x):
  words = sentence.split(" ")
  for i in words:
    if len(i) < x:
      return False
  return True

print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True


# Check Name
def check_for_name(sentence, name):
  return name.lower() in sentence.lower()


print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# Every Other Letter
def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print


# Reverse
def reverse_string(word):
  reverse = ""
  for i in range(len(word)):
    reverse += word[-i-1]
  return reverse

# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print


# Make Spoonerism
def make_spoonerism(word1, word2):

  two_words = ""
  two_words = word2[0] + word1[1:] + " " + word1[0] + word2[1:]

  return two_words


print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a


# Add Exclamation
def add_exclamation(word):
  while(len(word) < 20):
    word += "!"
  return word


print(add_exclamation("Codecademy"))
# should print Codecademy!!!!!!!!!!
print(add_exclamation("Codecademy is the best place to learn"))
# should print Codecademy is the best place to learn
