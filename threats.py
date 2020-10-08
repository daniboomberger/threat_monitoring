import praw
import json

#create log file to check to not send threats two times
#log_file = open('log.txt', 'w+')

#loading credentials from credentials.json
credentials_file = open('credentials.json', 'r')
credentials = json.load(credentials_file)

#reddit authentication
reddit = praw.Reddit(client_id=credentials['client_id'], \
                     client_secret=credentials['client_secret'], \
                     user_agent=credentials['user_agent'], \
                     username=credentials['username'], \
                     password=credentials['password'])

#filtered subreddit cybersecurity
cybersec_subreddit = reddit.subreddit('cybersecurity')
for threat in cybersec_subreddit.new(limit=5):
    #log_file.write(f'{threat.title} | {threat.url} | {threat.id}')
    print(f'{threat.title} | {threat.url} | {threat.id}')