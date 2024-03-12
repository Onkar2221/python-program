# condition = 
# ------------------- Century type year like 2000 --------------
# year % 400 == 0
# year  % 100 == 0     

# ------------------- Other than Century type year like 1996 , 2016 .. --------------
# year % 4 == 0
# year  % 100 != 0     


year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")
