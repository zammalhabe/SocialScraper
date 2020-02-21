import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen as uReq
import os
import json

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def ScrapTweets(user):
    print ('[+]' + G + ' Fetching Data From Twitter...' + '\n')
    link = "https://twitter.com/" + user
    the_client = uReq(link)
    page_html = the_client.read()
    the_client.close()

    soup = BeautifulSoup(page_html, 'html.parser')

    try:
        os.mkdir(user)
    except:
        pass
    f1=open("./{0}/{1}.txt".format(user,user),"w+")

    try:
        full_name = soup.find('a', attrs={"class": "ProfileHeaderCard-nameLink u-textInheritColor js-nav"})
        f1.write("\nUser Name --> " + str(full_name.text))
    except:
        f1.write("\nUser Name -->"+ R +" Not Found")

    try:
        user_id = soup.find('b', attrs={"class": "u-linkComplex-target"})
        f1.write("\nUser Id --> "+str(user_id.text))
    except:
        f1.write("\nUser Id --> "+"Not Found")

    try:
        decription = soup.find('p', attrs={"class": "ProfileHeaderCard-bio u-dir"})
        f1.write("\nDescription --> "+str(decription.text))
    except:
        f1.write("\nDecription not provided by the user")

    try:
        user_location = soup.find('span', attrs={"class": "ProfileHeaderCard-locationText u-dir"})
        f1.write("\nLocation -->  " +  str(user_location.text.strip()))
    except:
        f1.write("\nLocation not provided by the user")

    try:
        connectivity = soup.find('span', attrs={"class": "ProfileHeaderCard-urlText u-dir"})
        title = connectivity.a["title"]
        f1.write("\nLink provided by the user --> " + str(title))
    except:
        f1.write("\nNo contact link is provided by the user")

    try:
        join_date = soup.find('span', attrs={"class": "ProfileHeaderCard-joinDateText js-tooltip u-dir"})
        f1.write("\nThe user joined twitter on --> " + str(join_date.text))
    except:
        f1.write("\nThe joined date is not provided by the user")

    try:
        birth = soup.find('span', attrs={"class": "ProfileHeaderCard-birthdateText u-dir"})
        birth_date = birth.span.text
        f1.write("\nDate of Birth:"+str(birth_date.strip()))
    except:
        f1.write("\nBirth Date not provided by the user")

    try:
        span_box = soup.findAll('span', attrs={"class": "ProfileNav-value"})
        f1.write("\nTotal tweets --> " + span_box[0].text)
    except:
        f1.write("\nTotal Tweets --> Zero")

    try:
        f1.write("\nFollowing --> " +span_box[1].text)
    except:
        f1.write("\nFollowing --> Zero")

    try:
        f1.write("\nFollowers --> " + span_box[2].text)
    except:
        f1.write("\nFollowers --> Zero")

    try:
        f1.write("\nLikes send by him --> " + span_box[3].text)
    except:
        f1.write("\nLikes send by him --> Zero")

    try:
        if span_box[4].text != "More ":
            f1.write("\nNo. of parties he is Subscribed to --> " + span_box[4].text)
        else:
            f1.write("\nNo. of parties he is Subscribed to --> Zero")
    except:
        f1.write("\nNo. of parties he is Subscribed to --> Zero")
    f1.write(W)

    spana = soup.findAll('span', attrs={"class": "ProfileNav-value"})

    f1.write("\nTweets by "+ str(user) + " are --> ")

    for tweets in soup.findAll('p', attrs={"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"}):
        f1.write(tweets.text)
        f1.write("\n")
    f1.close()
