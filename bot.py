import sys
import twitter, os, time, random

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

# open file in read mode
file = open("bond.txt", "r")
contentbond=[]

# read file line by line and store lines to a list
for line in file:
	contentbond.append(line)

# open file in read mode
file = open("eyre.txt", "r")
contenteyre=[]

# read file line by line and store lines to a list
for line in file:
	contenteyre.append(line)

# select a tweet at random and cut of the \n in the end
tweet = (random.choice(contentbond)[:-1]) + (random.choice(contenteyre)[:-1])
print tweet
if len(tweet) < 130:
    api.PostUpdate(tweet)
else:
    numtweets = int(round((len(tweet)/130)+.5))
    curtweet = 1
    startcut = 0
    endcut = 130
    for i in range(1,numtweets+1):
        newtweet = tweet[startcut:endcut]
        api.PostUpdate('(' + str(curtweet) + '/' + str(numtweets) + ') ' + newtweet)
        curtweet = curtweet + 1
        startcut = startcut + 130
        endcut = endcut + 130
