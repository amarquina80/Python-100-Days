
daysThisYear = int(input("How many days are in this year? "))

daysInYear = 365
daysInLeapyear = 366
hoursInDay = 24
minutesInHour = 60
secondsInMinute = 60


regularYear = daysThisYear * hoursInDay * minutesInHour * secondsInMinute

leapYear = daysInLeapyear * hoursInDay * minutesInHour * secondsInMinute


if daysThisYear == 366:
  print("It is leap year! There are", leapYear, "seconds this year.")
elif daysThisYear == 365:
  print("There are", regularYear, "seconds this year...")
else:
  print("there are either 365 or 366 days in a year, try again.")