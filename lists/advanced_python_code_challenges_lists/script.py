#Every Three Numbers
def every_three_nums(start):
  return list(range(start, 101, 3))

print(every_three_nums(91))


# Remove the Middle
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))


#More Frequent Item
def more_frequent_item(lst, item1, item2):

  if(lst.count(item1) >= lst.count(item2)):
    return item1
  else:
    return item2


print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))


# Double Index
def double_index(lst, index):

  if(index >= len(lst)):

    return lst
  else:
    new_lst = lst[0:index]
    new_lst.append(lst[index] * 2)
    new_lst += lst[index + 1:]

    return new_lst

print(double_index([3, 8, -10, 12], 2))

# Middle Element
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))
