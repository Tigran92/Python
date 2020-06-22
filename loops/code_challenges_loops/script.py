# Divisible By Ten
def divisible_by_ten(nums):

  count = 0

  for i in nums:
    if (i%10 == 0):
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40]))


# Greetings
def add_greetings(names):

  new_list = []

  for name in names:

    new_list.append("Hello, " + name)
  return new_list

print(add_greetings(["Owen", "Max", "Sophie"]))


# Delete Starting Even Numbers
def delete_starting_evens(lst):

  while len(lst) >= 1 and (lst[0] % 2 == 0):

    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))


  # Odd Indices
def odd_indices(lst):

  new_list = []

  for i in range(1, len(lst), 2):
    new_list.append(lst[i])
  return new_list


print(odd_indices([4, 3, 7, 10, 11, -2]))


#Exponent
def exponents(bases, powers):

  new_list = []

  for i in bases:
    for j in powers:

      new_list.append(i**j)

  return new_list


print(exponents([2, 3, 4], [1, 2, 3]))


#Larger Sum
def larger_sum(lst1, lst2):

  sum_l1 = 0
  sum_l2 = 0

  for i in lst1:

    sum_l1 += i
  print(sum_l1)

  for j in lst2:

    sum_l2 += j
  print(sum_l2)

  if (sum_l1 >= sum_l2):
    return lst1
  else:
    return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))


# Over 9000
def over_nine_thousand(lst):
  sum_lst = 0
  for i in lst:
    sum_lst += i
    if (sum_lst > 9000):
      break
  return sum_lst


print(over_nine_thousand([8000, 900, 120, 5000]))


# Max Num
def max_num(nums):

  cur_max = 0
  for i in nums:

    cur_max = nums[0]
    if (cur_max < i) or (len(nums) == 1):
      cur_max = i
      return cur_max


print(max_num([50, -10, 0, 75, 20]))


# Same Value
def same_values(lst1, lst2):

  pos_list = []

  for i in range(len(lst1)):
    if(lst1[i] == lst2[i]):

      pos_list.append(i)


  return pos_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


# Reversed List
def reversed_list(lst1, lst2):

  for i in range(len(lst1)):
    if lst1[i] != lst2[len(lst2) - 1 - i]:
      return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
