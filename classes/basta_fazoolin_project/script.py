class Menu:

  def __init__(self, name, items, start_time, end_time):

    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_tiem = end_time



brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

brunch = Menu('Brunch', brunch_items, 1100, 1600)

print(brunch.name)

    
