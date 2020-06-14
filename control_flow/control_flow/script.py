#Boolean Variables
my_baby_bool = "true"

print(type(my_baby_bool))

my_baby_bool_two = True

print(type(my_baby_bool_two))


#If Statements
def dave_check(user_name):
  if user_name == "Dave":
    return "Get off my computer Dave!"

  if user_name == "angela_catlady_87":
    return "I know it is you Dave! Go away!"


# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

print(dave_check(user_name))


#Relational Operations II
def greater_than(x, y):
  if x > y:
    return x

  if y > x:
    return y

  if x == y:
    return "These numbers are the same"


def graduation_reqs(credits):
  if credits >= 120:
    return "You have enough credits to graduate!"


print(graduation_reqs(120))


#Boolean Operators: and
statement_one = False

statement_two = True

def graduation_reqs1(gpa, credits):
  if credits >= 120 and gpa >= 2.0:
    return "You meet the requirements to graduate!"

print(graduation_reqs1(3, 130))


#Boolean Operators: or
statement_one = True

statement_two = True

def graduation_mailer(gpa, credits):
  if credits >= 120 or gpa >= 2:
    return True

print(graduation_mailer(3, 114))


#Boolean Operators: not
statement_one = False

statement_two = True

def graduation_reqs2(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"

  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."

  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."

  if not (gpa >= 2.0) and not (credits >= 120):
    return "You do not meet either requirement to graduate!"

print(graduation_reqs2(1, 120))


def graduation_reqs3(gpa, credits):
  if (gpa >= 2.0) and (credits >= 120):
    return "You meet the requirements to graduate!"
  if (gpa >= 2.0) and not (credits >= 120):
    return "You do not have enough credits to graduate."
  if not (gpa >= 2.0) and (credits >= 120):
    return "Your GPA is not high enough to graduate."
  else:
    return "You do not meet the GPA or the credit requirement for graduation."

print(graduation_reqs3(1, 110))


#Else If Statements
def grade_converter(gpa):
  grade = gpa

  if (grade >= 4):
    return "A"
  elif (grade >= 3):
    return "B"
  elif (grade >= 2):
    return "C"
  elif (grade >= 1):
    return "D"
  else:
    return "F"

  return grade

print(grade_converter(0))


#Try and Except Statements
def raises_value_error():
  raise ValueError

try:
  raises_value_error()
except ValueError:
  print("You raised a ValueError!")



def applicant_selector(gpa, ps_score, ec_count):

    if (gpa >= 3.0) and (ps_score >= 90) and (ec_count >= 3):
        return "This applicant should be accepted."

    elif (gpa >= 3.0) and (ps_score >= 90) and not (ec_count >= 3):
        return "This applicant should be given an in-person interview."

    else:
        return "This applicant should be rejected."



print(applicant_selector(3.3, 98, 2))
