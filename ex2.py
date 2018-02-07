import urllib
import json
import datetime

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

cun_date=datetime.datetime.now().date()
m=cun_date.month
y=cun_date.year
if m==2:
    if y%4==0:
        if y%100!=0:
            months[m]['days']+=1
        elif y%400==0:
            months[m]['days']+=1

flag=False
while flag==False:
    usernumbers = raw_input("\nGive 10 different Numbers:(seperated by space) ")
    usernumbers = usernumbers.split()
    usernumbers = [int(number) for number in usernumbers]
    if len(usernumbers)==10:
        break
#snc = same number counter
def compare_lists(l1,l2):
    snc=0
    for i in l1:
        if i in l2:
            snc+=1
    return snc

cmw=0 # cmw = current maximun wins (of a day)
cmwday=0
for day in range(1,months[m]['days']+1):
    wins=0
    #print 'Results for:',day,months[m]['name'],y
    url = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/%d-%d-%d.json" % ( day , m , y )
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    klhrwseis= data['draws']['draw']
    ml=[] #mixed_lists
    for k in klhrwseis:
        temp=k["results"]
        ml.append(compare_lists(usernumbers ,temp))
    #print ml
    for number in ml:
        if number>4:
            wins+=1
    if wins>=cmw:
        cmw=wins
        cmwday=day
print '\nBest day of',months[m]['name'],y,'is:',cmwday,'with',cmw,'wins!'
