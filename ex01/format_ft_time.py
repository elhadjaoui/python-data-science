import datetime

now = datetime.datetime.now()
print('Seconds since January 1, 1970: {:,.4f}'.format(now.timestamp()), 'or', format(now.timestamp(), 'e'), 'in scientific notation') # https://www.w3schools.com/python/ref_string_format.asp
print(now.strftime('%b %m %Y') ) # https://www.w3schools.com/python/python_datetime.asp