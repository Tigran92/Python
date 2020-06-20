#Append Sum
def append_sum(lst):
  add_lst = lst[-1] + lst[-2]
  lst.append(add_lst)
  add_lst = lst[-1] + lst[-2]
  lst.append(add_lst)
  add_lst = lst[-1] + lst[-2]
  lst.append(add_lst)

  return lst


print(append_sum([1, 1, 2]))


#Largest List
def larger_list(lst1, lst2):

  if (len(lst1) > len(lst2)):
    return lst1[-1]
  elif(len(lst2) > len(lst1)):
    return lst2[-1]
  else:
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))


#More Than n
def more_than_n(lst, item, n):

  if(lst.count(item) > n):
    return True
  else:
    return False


print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


#Append Size
def append_size(lst):

  size = len(lst)

  lst.append(size)

  return lst

print(append_size([23, 42, 108]))


#Combine Sort
def combine_sort(lst1, lst2):

  new_lst = lst1 + lst2

  new_lst.sort()

  return new_lst

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
