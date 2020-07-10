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


# What Is a CSV File?
path = os.path.join(my_path, "../files/logger.csv")
with open(path) as log_csv_file:

  print(log_csv_file.read())


# Reading a CSV File
import csv

path = os.path.join(my_path, "../files/cool_csv.csv")
with open(path) as cool_csv_file:

  cool_csv_dict = csv.DictReader(cool_csv_file)

  for cool_fact in cool_csv_dict:

    print(cool_fact['Cool Fact'])


# Reading Different Types of CSV Files
path = os.path.join(my_path, "../files/books.csv")
with open(path, newline='') as books_csv:

  books_reader = csv.DictReader(books_csv, delimiter='@')

  isbn_list = []

  for isbn in books_reader:

    isbn_list.append(isbn['ISBN'])
  print(isbn_list)


# Writing a CSV File
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

path = os.path.join(my_path, "../files/loggers.csv")
with open(path, 'w') as logger_csv:

  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)

  log_writer.writeheader()
  for element in access_log:

    log_writer.writerow(element)


# Reading a JSON File
import json

path = os.path.join(my_path, "../files/message.json")
with open(path) as message_json:

  message = json.load(message_json)

  print(message['text'])


# Writing a JSON File
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

path = os.path.join(my_path, "../files/data.json")
with open(path, 'w') as data_json:

  json.dump(data_payload, data_json)
