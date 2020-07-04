letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key, value in zip(letters, points)}
print(letter_to_points)

letter_to_points[" "] = 0
print(letter_to_points)

def score_word(word):

  point_total = 0
  for i in word:
    point_total += letter_to_points.get(i,0)
  return point_total

print_total_points = score_word("WoRd")
print(print_total_points)