# Get Calendar Day program
# Query any date for the name of the weekday (earliest date: 1st January 1930)
# Written without using any date/time modules as a simple coding challenge...

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and not year % 400 == 0:
            return False
        else:
            return True
    else:
        return False

def get_day(year, month, date):
    days = [
            "Wednesday", 
            "Thursday", 
            "Friday",
            "Saturday", 
            "Sunday", 
            "Monday", 
            "Tuesday", 
            ]

    months = {
                1: "Jan",
                2: "Feb",
                3: "Mar",
                4: "Apr",
                5: "May",
                6: "Jun",
                7: "Jul",
                8: "Aug",
                9: "Sep",
                10: "Oct",
                11: "Nov",
                12: "Dec"
             }

    month_days = {
                    "Jan": 31, 
                    "Feb": 28, 
                    "Mar": 31, 
                    "Apr": 30,
                    "May": 31,
                    "Jun": 30,
                    "Jul": 31,
                    "Aug": 31,
                    "Sep": 30,
                    "Oct": 31,
                    "Nov": 30,
                    "Dec": 31
                 }

    # catalyst date: sat, jan 1 1930
    def_y = 1930
    def_m = 1
    cur_y = def_y
    cur_m = def_m
    delta_y = 0
    d_count = 0
    d_index = 0
    
    if year > def_y:
        delta_y = year - def_y

    # main loop
    for y in range(delta_y + 1):
        # check if current year is leap year
        leap_year = is_leap_year(cur_y)
        if leap_year:
            month_days["Feb"] = 29
            year_days = 366
        else:
            month_days["Feb"] = 28
            year_days = 365

        # if current year is target year, cycle months
        if cur_y == year:
            for m in range(month):
                vmonth = months.get(cur_m)
                # if month is target month, cycle days...
                if cur_m == month:
                    for d in range(date):
                        d_index = d_count % 7
                        d_count += 1
                    return days[d_index]
                    # return days[d_index]
                else:
                    d_count += month_days.get(vmonth)
                    if cur_m < 12:
                        cur_m += 1
        # cycle years
        elif delta_y > 0:
            d_count += year_days
            delta_y -= 1
            cur_y += 1

# validation
y_valid = False
m_valid = False
d_valid = False

# input year
while y_valid != True:
    try:
        input_y = int(input("Enter Year: "))
        if (input_y >= 1930) and (input_y <= 9999):
            y_valid = True
            leap_year = is_leap_year(input_y)
        else:
            print("Must be between 1930 - 9999")
    except:
        print("Must be a number...")

# input month
while m_valid != True:
    try:
        input_m = int(input("Enter Month (1-12): "))
        if (input_m >= 1) and (input_m <= 12):
            m_valid = True
        else:
            print("Must be a number between 1 - 12")
    except:
        print("Must be a number...")

# input day
while d_valid != True:
    # check valid inputs per month / leap year. designate ceiling
    m_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
              7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if leap_year:
        m_days[2] = 29
    ceil = m_days.get(input_m)

    try:
        input_d = int(input(f"Enter Day (1-{ceil}): "))
        if (input_d >= 1) and (input_d <= ceil):
            d_valid = True
        else:
            print(f"Must be a number between 1 - {ceil}")
    except:
        print("Must be a number...")


# call main function / output
your_day = get_day(input_y, input_m, input_d)

print(f"\nWeekday of {input_d}/{input_m}/{input_y} = {your_day}")
