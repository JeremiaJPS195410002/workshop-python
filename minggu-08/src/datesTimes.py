from datetime import date
now = date.today()
now
#datetime.date(2022, 4, 19) (output)

now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
#'04-19-22. 19 Apr 2022 is a Tuesday on the 19 day of April.' (output)

birthday = date(1964, 7, 31)
age = now - birthday
age.days
#21081 (output)