def is_leap_year(a_year):  
 """ a function to return if the given year is a leap year """
 if a_year % 400 == 0 and a_year % 100 == 0:
   print(a_year, "is a leap year")
 # not divided by 100 means not a century year
 # year divided by 4 is a leap year
 elif a_year % 4 ==0 and a_year % 100 != 0:
    print(a_year, "is a leap year")
 else:
   print(a_year, "is not a leap year")
is_leap_year(2018)