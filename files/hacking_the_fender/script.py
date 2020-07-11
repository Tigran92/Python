import os.path
import csv

# getting the relative paths
my_path = os.path.abspath(os.path.dirname(__file__))
# Reading a File
path = os.path.join(my_path, "../hacking_the_fender/passwords.csv")

compromised_users = []

with open(path) as password_file:

  password_csv = csv.DictReader(password_file)

  for password_row in password_csv:

    print(password_row['Username'])
