## Reddit Webscraper 2.0
## Designed by Julian Marks
## June 2017

import sys
import io							# Interface with Users
import os							# Interface with Operating System
import requests						# Make HTTP/API requests
import time							# Time the length of function calls
from PIL import Image						# Useful to open and view images
# import tkinter					# Maybe useful for creating GUI Reddit interface
import praw						# Old library used for Reddit Authorization. Not needed now that basic auth is utilized.
# import matplotlib.pyplot as plt	# Useful to view data/statistics
from bs4 import BeautifulSoup

## Identification Information

USER_AGENT = 'Scraper 2.0 by /u/OrangeJulian12'
CLIENT_ID = ''
CLIENT_SECRET = ''
CLIENT_AUTH = requests.auth.HTTPBasicAuth(CLIENT_ID,CLIENT_SECRET)
USERNAME = ''
PASSWORD = ''


## Information to access API

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
AUTHORIZATION_BASE_URL = 'https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=TYPE&state=RANDOM_STRING&redirect_uri=URI&duration=DURATION&scope=SCOPE_STRING'

POST_DATA = {"grant_type":"password", "username":USERNAME, "password":PASSWORD}
HEADERS = {"User-Agent":USER_AGENT}


## Global Program Parameters

SCORE = 200000
HIT_COUNT = 50
sub_reddits = ["pics"]
subreddit_dict = {}

## For Praw
sub_reddit='pics'


print('------------------- Program Start -------------------\n')

Red = requests.post(TOKEN_URL, auth=CLIENT_AUTH, data = POST_DATA, headers=HEADERS)
# print(Red.json())
ACCESS_TOKEN = Red.json()["access_token"]

HEADERS = {"Authorization":"bearer "+ACCESS_TOKEN, "User-Agent" : USER_AGENT}
Red = requests.get("https://oauth.reddit.com/", headers=HEADERS)
# print(Red.json())
# print(Red.text)


# print(Red.status_code)
# print(Red.headers['content-type'])
# print(Red.encoding)
# print(Red.url)
# Red = requests.get("https://www.reddit.com/")

# soup = BeautifulSoup(Red.text,'html.parser')
# print(soup.prettify())


## This defines a connection to reddit, which can be used as a variable to access different subsections of reddit.

reddit = praw.Reddit(client_id = CLIENT_ID,
	client_secret = CLIENT_SECRET,
	user_agent = USER_AGENT)


## Parses the subreddit into submissions, which have the following variables.
## Not necessarily efficient, but I've included a way to convert the image into a format
## that can be read by Python and opened by an app on your computer.


## This generator function controls the parse to only extract HIT_COUNT number of entries,
## and out of those entries it only returns ones with with a score > SCORE. (Number of upvotes on a post)

gen = (x for x in reddit.subreddit(sub_reddit).hot(limit=HIT_COUNT) if x.score > SCORE)


# file = open(FILENAME, 'w',encoding="utf8")

# scope = ['https://www.reddit.com/api/v1/authorize?client_id=CLIENT_ID&response_type=TYPE&state=RANDOM_STRING&redirect_uri=URI&duration=DURATION&scope=SCOPE_STRING']

# oauth = OAuth2Session(CLIENT_ID, redirect_uri = REDIRECT_URI, scope = scope)
# AUTHORIZATION_URL, state = oauth.authorization_url(AUTHORIZATION_BASE_URL)
# session['oauth_state'] = state


# oauth = OAuth2Session(client = LegacyApplicationClient(client_id=CLIENT_ID))
# token = oauth.fetch_token(token_url=TOKEN_URL,username=USERNAME, password=PASSWORD,client_id=CLIENT_ID, client_secret=CLIENT_SECRET,grant_type=authorization_code&code=CODE&redirect_uri=URI)
# authorization_url, state = oauth.authorization_url()



# file.close()
# FINALFILE = 'notepad.exe ' + FILENAME
# os.system(FINALFILE)



# for sub in sub_reddits:
# 	for submission in reddit.subreddit(sub).top(limit=HIT_COUNT):
# 		if "sql" in submission.title.lower():
# 			submission.info = submission.title + '\n' + submission.url + '\n \n'
# 			file.write(submission.info)




	# score_gen = (x.score for x in reddit.subreddit(sub).top(limit=HIT_COUNT))
	# subreddit_dict[sub] = list(score_gen)

	# print(sub,'\n',"Total Score = ", sum(subreddit_dict[sub]),'\n', 
	# 		"Average Score = ", sum(subreddit_dict[sub])/len(subreddit_dict[sub]), '\n')


## Here we can look at how to compare results and plot graphs with one another

# for key in subreddit_dict.keys():
# 	plt.plot(subreddit_dict[key])
# 	plt.show()


# root = Tk()

for submission in gen:
	print(submission.title, '\n',
	submission.score, '\n',
	submission.id, '\n',
	submission.url, '\n',
	'------------------------------------', '\n')

	if '.jpg' in submission.url or '.jpeg' in submission.url or '.png' in submission.url:
		image = Image.open(requests.get(submission.url, stream=True).raw)
		image.show()
	# elif '.gif' in submission.url:

		# frames = [PhotoImage(file=submission.url ,format = 'gif -index %i' %(i)) for i in range(100)]


