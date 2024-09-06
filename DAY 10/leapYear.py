def is_leap_year_2(year):
    if year % 400 == 0:
        print("here")
        return True
    else:
        return False

def is_leap_year_1(year):
    if year % 100 == 0:
       return True
    else:
       return is_leap_year_2(year)

def is_leap_year(year):
    if year % 4 == 0:
       return is_leap_year_1(year)
    else:
        return False




leapYear = is_leap_year(2100)
print(leapYear)