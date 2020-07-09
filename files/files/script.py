import os.path

# getting the relative paths
my_path = os.path.abspath(os.path.dirname(__file__))
# Reading a File
path = os.path.join(my_path, "../files/welcome.txt")
with open(path) as text_file:


  text_data = text_file.read()
print(text_data)


# Iterating Through Lines
path = os.path.join(my_path, "../files/how_many_lines.txt")
with open(path) as lines_doc:

  for line in lines_doc.readlines():
    print(line)


# Reading a Line
path = os.path.join(my_path, "../files/just_the_first.txt")
with open(path) as first_line_doc:

  first_line = first_line_doc.readline()
  print(first_line)


# Writing a File
path = os.path.join(my_path, "../files/bad_bands.txt")
with open(path, 'w') as bad_bands_doc:

  bad_bands = bad_bands_doc.write('DISLIKE')
  bad_bands1 = bad_bands_doc.write('LIKE')


# Appending to a File
path = os.path.join(my_path, "../files/cool_dogs.txt")
with open(path, 'a') as cool_dogs_file:

  cool_dogs_file.write('It/s repeating?')


# What's With "with"?
path = os.path.join(my_path, "../files/fun_file.txt")
with open(path) as close_this_file:

  setup = close_this_file.readline()
  punchline = close_this_file.readline()

print(setup)
