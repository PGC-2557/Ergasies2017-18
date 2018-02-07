
y=int(raw_input("Give a Year: "))
m=int(raw_input("Give a Month (In Number): "))

if m ==1:   #apetish ths formoulas
    m+=12
    y-=1
elif m==2:
    m+=12
    y-=1

x=((1 + 2*m + int((3*(m+1))/5) + y + int(y/4) - int(y/100) + int(y/400) + 2))%7

if x==0:
    x=7

months={
1:{'name':'January','days':31}
,2:{'name':'February','days':28}
,3:{'name':'March','days':31}
,4:{'name':'April','days':30}
,5:{'name':'May','days':31}
,6:{'name':'June','days':30}
,7:{'name':'July','days':31}
,8:{'name':'August','days':31}
,9:{'name':'September','days':30}
,10:{'name':'October','days':31}
,11:{'name':'November','days':30}
,12:{'name':'December','days':31}
}

if m ==13:
    m-=12
    y+=1
elif m==14:
    m-=12
    y+=1

if months[m]['name']=="February":
    if y%4==0:                 #koitaei an einai disekto etos
        if y%100!=0:
            end=months[m]['days']+1
        elif y%400==0:
            end=months[m]['days']+1
        else:
            end=months[m]['days']
    else:
        end=months[m]['days']
else:
    end=months[m]['days']



print"\n",months[m]['name'],y
print"S\tM\tT\tW\tT\tF\tS"
counter=0  #metra ka8e pote allazei h vdomada wste na alla3ei grammh kai stous ari8mous
counter2=0 #metra poses fores den egra3e tipota (epese sthn prwth periptwsh)
dayprinter=1  #anevenei apoklistika opote typwnei mia hmerominia
for i in range (1,end+6+1): #  +6 giati einai o megistos ari8mos extra kinisewn p 8a eprepe
    counter+=1                 # na kanei to programma gia na arxisei ton mina sthn swsth mera (dld to savvato)
    if i<x or i>=end+1+counter2 :       #kai olo auto gia na mhn xasw tis teleftees meres tou mina
        counter2+=1
        if counter%7==0:
            print "  \t"         #afinei kena
        else:
            print "  \t",
    else:
        if counter%7==0:
            print dayprinter,"\t"
            dayprinter+=1
        else:
            print dayprinter,"\t",
            dayprinter+=1
