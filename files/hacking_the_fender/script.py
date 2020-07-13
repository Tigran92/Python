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

      compromised_users.append(password_row['Username'])

  print(compromised_users)

# Reading a File
path = os.path.join(my_path, "../hacking_the_fender/compromised_users.txt")
with open(path, 'w') as compromised_user_file:

  for users in compromised_users:

    compromised_user_file.write(users)

import json

path = os.path.join(my_path, "../hacking_the_fender/boss_message.json")
with open(path, 'w') as boss_message:

  boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}

  json.dump(boss_message_dict, boss_message)

path = os.path.join(my_path, "../hacking_the_fender/new_passwords.json")
with open(path, 'w') as new_passwords_obj:

  slash_null_sig = """_  _     ___   __  ____
/ )( \   / __) /  \(_  _)
) \/ (  ( (_ \(  O ) )(
\____/   \___/ \__/ (__)
 _  _   __    ___  __ _  ____  ____
/ )( \ / _\  / __)(  / )(  __)(    \
) __ (/    \( (__  )  (  ) _)  ) D (
\_)(_/\_/\_/ \___)(__\_)(____)(____/
        ____  __     __   ____  _  _
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __
(  ( \/ )( \(  )  (  )
/    /) \/ (/ (_/\/ (_/\
\_)__)\____/\____/\____/"""

  new_passwords_obj.write(slash_null_sig)
