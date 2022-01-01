import math #匯入math模組

#輸入年份、月份
year=int(input("請輸入年份:"))
month=int(input("請輸入月份:"))

Year=year #使用者輸入的原始年份(未經過計算)

#計算當月天數
if (month==1)|(month==3)|(month==5)|(month==7)|(month==8)|(month==10)|(month==12):
    totalDays=31
elif month==2:
    if (year%400==0)|((year%4==0)&(year%100!=0)):
        totalDays=29
    else:
        totalDays=28
else:
    totalDays=30        

#若輸入月份為1、2月，則必須看作前一年的13、14月來做計算。ex:2020年1月 ==> 2019年13月
if (month==1)|(month==2):
    year=year-1

c=year//100 #年份前兩位數
y=year%100 #年份後兩位數
a=[13,14,3,4,5,6,7,8,9,10,11,12] #各月份所對應數值
m=a[month-1]
d=1 #day，每個月的1號

#蔡勒公式（Zeller's congruence），計算每月1號屬一星期中哪一日
if ((Year==1582)&(month<=10))|(Year<1582):
    week=(y+math.floor(y/4)-c+math.floor(26*(m+1)/10)+d+4)%7
else:
    week=(y+math.floor(y/4)+math.floor(c/4)-2*c+math.floor(26*(m+1)/10)+d-1)%7

#印出萬年曆
#1582年10月4日或之前為儒略曆，1582年10月5日到10月14日這十天在歷史上不存在
print("日\t一\t二\t三\t四\t五\t六")
if (Year==1582)&(month==10):
    print("  \t",end='')
    count=1
    for i in range(1,5):
        print(i,"\t",end='')
        count=count+1
    for i in range(15,32):
        print(i,"\t",end='')
        count=count+1
        if count%7==0:
            print("\n")
else:
    count=week
    for i in range(week):
        print("  \t",end='')
    for i in range(1,totalDays+1):
        print(i,"\t",end='')
        count=count+1
        if count%7==0:
            print("\n")