import datetime

week2day = {
    "Monday"    : 1,
    "Tuesday"   : 2,
    "Wednesday" : 3,
    "Thursday"  : 4,
    "Friday"    : 5,
    "Saturday"  : 6,
    "Sunday"    : 7
}
num2weeknum = {
    "1st" : 1,
    "2nd" : 2,
    "3rd" : 3,
    "4th" : 4,
    "5th" : 5
}
day_candi = [13,16,19]
def meetup_day(year, month, week, num):
    if num == "last":
        date = __meetup_day(year, month, week, "1st")
        for num in [4,5]:
            date1 = date + datetime.timedelta(7*num)
            if date1.month != month:
                return date + datetime.timedelta(7*(num-1))
    elif num == "teenth":
        weekenday = week2day[week]
        for day in day_candi:
            date = datetime.date(year, month, day)
            if date.isoweekday() == weekenday:
                return date
    else:
       return __meetup_day(year, month, week, num)
def __meetup_day(year, month, week,num):
    start = datetime.date(year, month, 1)
    weekenday = week2day[week]
    weeknum = num2weeknum[num]
    startweek = start.isoweekday()
    if (startweek < weekenday):
        daydelta = weekenday - startweek + (weeknum - 1) * 7
    elif (startweek == weekenday):
        daydelta = 0 + (weeknum-1)*7
    else:
        daydelta = (weeknum -1)*7+7-startweek+weekenday
    return datetime.date(year,month,1+daydelta)


