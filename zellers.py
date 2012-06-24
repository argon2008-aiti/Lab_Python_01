#  YAYRA KOFI KETEKU
# program to receive input from user and output it back formated

user_First_Name = raw_input('Enter your first name:  ')     #Ask user's first name and save in user_First_Name

user_Last_Name = raw_input ('Enter your last name:  ')  #Ask user's last name and save in user_Last_Name
print

print 'Enter your date of birth:'                       #Ask user's date of birth and save

Day = raw_input('Day?:')
Month = raw_input('Month(from 1-12 where march = 1, april =2 and february = 12 in that order):  ')
print

Year = raw_input('Year: ( subtract a year if you are born in january or february)  :')
print


const_A = Month
const_B = Day

if len(Year) == 4:
    const_C = Year[2:]
    const_D = Year[:2]

if len(Year) == 3:
    const_C = Year[2:]
    const_D = Year[:1]

if len(Year) <= 2:
    const_C = Year
    const_D = '0'

#define constants to help compute the day of the week

var_W = (13*int(const_A)-1)/5

var_X = int(const_C)/4

var_Y = int(const_D)/4

var_Z = var_W + var_X + var_Y + int(const_B) + int(const_C)-2*int(const_D)

var_R = var_Z%7
while var_R < 0:
     var_R = var_R + 7

Days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'] # form a list of days

birth_Day = Days[var_R]


print "{0} {1} was born on {2}".format(user_First_Name,user_Last_Name,birth_Day)  #print user's data

