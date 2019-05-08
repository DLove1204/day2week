def split_day(str_day):         #str_day format is 20010105
    year,month,day = str_day[0:4],str_day[4:6],str_day[6:]


    return year,month,day


monthcode1_dict = {"01":6,"02":2,"03":2,"04":5,"05":0,"06":3,    \
                   "07":5,"08":1,"09":4,"10":6,"11":2,"12":4} #ping year
monthcode2_dict = {"01":5,"02":1,"03":2,"04":5,"05":0,"06":3,    \
                   "07":5,"08":1,"09":4,"10":6,"11":2,"12":4} # rvn year

week_dict = {"0":"星期日","1":"星期一","2":"星期二","3":"星期三","4":"星期四","5":"星期五","6":"星期六"}



def main(x):
    if len(x) != 8:
        print("please check the the day_input form,it must be like yyyymmdd")
        print("y,m,d are year,month,day")
        return -1
    a,b,c = split_day(x)
    daycode = int(c)
    year = int(a)
    if year %100 == 0:
        if year % 400 == 0:
            monthcode = monthcode2_dict[b]
        else:
            monthcode = monthcode1_dict[b]
    else:
        if year % 4 == 0:
            monthcode = monthcode2_dict[b]
        else:
            monthcode = monthcode1_dict[b]
    year_2nd = a[2:]
    year_2nd_int = int(year_2nd )
    yearcode = (int(year_2nd_int/4)+year_2nd_int) % 7


    all = daycode +monthcode +yearcode
    index = str(all %7)
    xingqi = week_dict[index]
    print(xingqi)
    return xingqi

if __name__ == '__main__':
    str_day = "20191102"
    xingqi = main(str_day)