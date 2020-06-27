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
