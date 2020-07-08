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
