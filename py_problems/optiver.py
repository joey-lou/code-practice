# some optiver problems
import datetime as dt


def days_in_month(year: int, month: int) -> int:
    if month == 12:
        next_year = year + 1
        next_month = 1
    else:
        next_year = year
        next_month = month + 1

    return (dt.date(next_year, next_month, 1) - dt.date(year, month, 1)).days


def days_between(inputs: list):
    assert len(inputs) == 6
    start_year, start_month, start_day = (int(i) for i in inputs[:3])
    end_year, end_month, end_day = (int(i) for i in inputs[3:])

    year = start_year
    month = start_month

    days = 0
    while year < end_year or month <= end_month:
        days += days_in_month(year, month)
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

    days -= start_day
    days -= days_in_month(end_year, end_month) - end_day

    return days


print(days_between([2024, 1, 3, 2024, 1, 6]))
print(days_between([2010, 1, 5, 2011, 1, 5]))
print(days_between([2024, 1, 3, 2024, 1, 4]))
