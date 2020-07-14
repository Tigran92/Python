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
