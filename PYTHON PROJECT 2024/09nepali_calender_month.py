import datetime
import datetime_nepali

year =int(input("enter the english year :"))
month =int(input("enter the english month :"))
day =int(input("enter the english day :"))
calender= datetime_nepali.date(year, month, day).calendar()
print(calender) 