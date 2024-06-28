import datetime
import datetime_nepali

year =int(input("enter the english year :"))
month =int(input("enter the english month :"))
day =int(input("enter the english day :"))
date =datetime_nepali.date.from_datetime_date(datetime.date(year, month, day))
print(f"the nepali date is :{date} B.S")