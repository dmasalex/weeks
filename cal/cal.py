from datetime import datetime
from isoweek import Week

main_date = datetime(2019, 1, 1)
calculated_date = datetime(2019, 12, 9)

def count_week(year):
    return Week.last_week_of_year(year).week


def date_week(date):
    return Week.withdate(date)

count = 0
difference = calculated_date.year - main_date.year

if difference == 0:
    c = date_week(calculated_date)
    count = Week.__str__(c)[-2:]
else:
    for c in range(1, difference + 1):
        print(main_date.year + c)
        if main_date.year + c != calculated_date.year:
            c = count_week(main_date.year + c)
            count += c
        else:
            tmg = ''
            c = date_week(calculated_date)
            tmp = Week.__str__(c)
            count += int(tmp[-2:])

print(count)
