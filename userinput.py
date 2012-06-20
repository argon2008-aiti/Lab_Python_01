#  YAYRA KOFI KETEKU
# program to receive input from user and output it back formated

user_First_Name = raw_input('Enter your first name:  ')     #Ask user's first name and save in user_First_Name

user_Last_Name = raw_input ('Enter your last name:  ')  #Ask user's last name and save in user_Last_Name
print

print 'Enter your date of birth:'                       #Ask user's date of birth and save

Day = raw_input('Day?:')
Month = raw_input('Month(from 1-12 where march = 1, april =2 and february = 12 in that order):  ')
print

Year = raw_input('Year: (add an extra year if you are not born in january or february)  :')
print

print "{0} {1} was born on {2} {3}, {4}".format(user_First_Name,user_Last_Name,Month,Day,Year)  #print user's data

