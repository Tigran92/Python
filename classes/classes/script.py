# Types
print(type(5))

my_dict = {}

print(type(my_dict))

my_list = []

print(type(my_list))


# Object-Oriented Programming
class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)


# Methods
class Rules:

  def washing_brushes(self):

    return "Point bristles towards the basin while washing your brushes."


# Methods with Arguments
class Circle:

  pi = 3.14

  def area(self, radius):

    return self.pi * radius ** 2


circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

print(pizza_area)
print(teaching_table_area)
print(round_room_area)


# Constructors
class Circle1:
  pi = 3.14

  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))

teaching_table = Circle1(36)


# Instance Variables
class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"


# Attribute Functions
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))


# Self
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:

    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza1 = Circle(12)
teaching_table1 = Circle(36)
round_room1 = Circle(11460)

print(medium_pizza1.circumference())
print(teaching_table1.circumference())
print(round_room1.circumference())


# Everything is an Object
check_dir = dir(5)
print(check_dir)

def this_function_is_an_object(test):

  return "hello"+test

print(dir(this_function_is_an_object))

# String Representation
class Circle:
  pi = 3.14

  def __init__(self, diameter):
    self.radius = diameter / 2

  def area(self):
    return self.pi * self.radius ** 2

  def circumference(self):
    return self.pi * 2 * self.radius

  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


class Student:

  def __init__(self, name, year):

    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65

  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))
