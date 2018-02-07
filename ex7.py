
import datetime

now = datetime.datetime.now()
y=now.year
m=now.month
d=now.day
c1=0
leapyear=False
for i in range(0,11):

    if m==2 and d==29: #leap year check
        if y%4==0:
            if y%100!=0:
                leapyear=True
            elif y%400==0:
                leapyear=True
            else:
                leapyear=False
        else:
            leapyear=False

    if (d!=29 and m!=2) or (d==29 and m==2 and leapyear==True): #this must not run if the day 29Feb and the year is not a leap.
        if m ==1:
            m+=12
            y-=1
        elif m==2:
            m+=12
            y-=1

        x=((d + 2*m + int((3*(m+1))/5) + y + int(y/4) - int(y/100) + int(y/400) + 2))%7

        if x==0:
            x=7
        if m ==13:
            m-=12
            y+=1
        elif m==14:
            m-=12
            y+=1


        if i==0:
            thebigday=x
        elif x==thebigday:
            c1+=1
    y+=1
here=datetime.date.today()
print "The date is",here.strftime("%d/%m/%y")
print "There will be the exact same day and date:",c1,"time(s) in the next 10 years."
