month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True :
    date_input = input("Date: ")
    if "/" in date_input :
        month_input, day, year = date_input.strip().replace(",", "").split("/")
        try :
            month_numbered = int(month_input)
            day_numbered = int(day)
            year_numbered = int(year)
            if month_numbered > 12 or day_numbered > 31:
                pass
            else :
                print(f"{year}-{month_numbered:02}-{day_numbered:02}")
                break
        except (TypeError, ValueError):
            pass
    elif " " in date_input and "," in date_input:
        month_input, day, year = date_input.strip().replace(",", "").split(" ")
        try :
            month_numbered = int(month.index(month_input) + 1)
            day_numbered = int(day)
            year_numbered = int(year)
            if month_numbered > 12 or day_numbered > 31:
                pass
            else :
                print(f"{year}-{month_numbered:02}-{day_numbered:02}")
                break
        except (TypeError, ValueError):
            pass
        else :
            pass
    else :
          pass
