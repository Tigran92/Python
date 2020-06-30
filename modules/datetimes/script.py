from datetime import datetime

# Datetime
birthday = datetime(1999, 10, 11, 4, 25, 12)
birthday.year
birthday.month
birthday.day
birthday.hour
# weekdays are represented by numbers 0-6
print(birthday.weekday())
print(birthday)


# Datetime.now() & Subtraction
datetime.now()
print(datetime.now())

date_difference = datetime(2018, 1, 1) - datetime(2017, 1, 1)
date_now_difference = datetime.now() - datetime(2017, 1, 1)
print(date_difference)
print(date_now_difference)

# Parsing datetime strptime
parsed_date = datetime.strptime('Jun 15, 2020', '%b %d, %Y')
print(parsed_date.month)
print(parsed_date.day)
print(parsed_date.year)


# Format a string based of datetime.  strftime
# uncomment the line below and comment strptime
# format_string = datetime.(datetime.now(),'%b %d, %Y')
# print(format_string)
