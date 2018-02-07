import tweepy
import re



print 31*"-"
consumer_key='HTRoPo30AVfnIj6MlqzTcjAnO'
consumer_secret='uc1czUOedLNyZtdsxpFKKaZlOh33i0hgvuSuRXiz3cybHfCgB6'
access_token='960259015065337857-boMTZaY6tXWmVe4qYH6mZ9WJQ598Xm8'
access_token_secret='cUaQzjz8nOejeKysvyEejLWVj9enNwzSuCH1iOEbJioKq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

print '|Examples:@realDonaldTrump    |'
print '|         @ErgasiaPente       |'
print 31*"-"
print 'For IMPORTANT information type: info '
name='info'
flag=0
while name =='info' or name=='turnoff':
    name=raw_input('Give a username: ')
    if name=='info':
        print 'Gia na exei noima to programma,den metraei le3eis me 2 h ligoterous xaraktires.'
        print 'Gia na apenergopoih8ei auth h leitourgia gra3e : turnoff'
    elif name=='turnoff':
        flag=1
        print 'Switched to Off'


fullalltweets = api.user_timeline(screen_name =name,count = 10, tweet_mode="extended")

alltweets=[i.full_text for i in fullalltweets]
alltweets = [re.sub('\W+'," ", i ) for i in alltweets]
alltweets = [word.encode("utf8") for word in alltweets]
alltweets = [i.replace(i,i+' ') for i in alltweets]
str1=''
for i in alltweets:
    str1+="".join([i])
#print str1
ls1=str1.split()
ls1=[i.lower() for i in ls1]
#print ls1

max1=0
max1word=""
for i in ls1:
    counter1=0
    for j in ls1:
        if i!='https': #to avoid pictures
            if [i]==[j] and flag==1: #turnoff
                counter1+=1
            elif [i]==[j] and flag==0: #default
                if len(i)>2:
                    counter1+=1

    if counter1>=max1:
        max1word=i
        max1=counter1



if max1!=0 and max1!=1:
    print 'The most used word in the last 10 tweets of user',name,': '
    print '( %s ) and it was used: %s times.' %(max1word,max1)
else:
    print 'Name Found!'
    print 'Name given:',name
    print 'No words found that were used for more than one time in the last 10 tweets.'

print 30*"-"
