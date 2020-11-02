import keys
import tweepy as t
import json

auth = t.OAuthHandler(keys.api_key, keys.api_secret)

auth.set_access_token(keys.access_token, keys.secret_token)

api = t.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


tweets = api.search(q = 'vote', count = 3)
#print(tweets)
''''
#print user and text of tweet
for tweet in tweets:
    print(tweet.user.screen_name,':',tweet.text)


tweets = api.search(q = '#collegefootball', count = 3)

for tweet in tweets:
    print(tweet.user.screen_name,':',tweet.text)
'''
#places with trending topics

trends_available = api.trends_available() #a list of dictionaries

#print(len(trends_available))
#print(trends_available[:3])

world_trends = api.trends_place(id = 1)
#print(world_trends)

outfile = open('world_trends.json', 'w')
json.dump(world_trends, outfile, indent = 5)

trends_list = world_trends[0]['trends']
#print(trends_list)

trends_list = [x for x in world_trends[0]['trends'] if x["tweet_volume"]] #if x[tweetvol] defaults to true aka is not null
#print(trends_list)

from operator import itemgetter #allows us to use another key to specify sorting

trends_list.sort(key = itemgetter('tweet_volume'), reverse = True)

#print(trends_list[:5])

#for t in trends_list:
    #print(t['name'])

#create worldcloud of trending topics in NYC

from wordcloud import WordCloud

nyc_trends = api.trends_place(id = 2459115)

nyc_trends_list = [t for t in nyc_trends[0]['trends']]

nyc_trends_list.sort(key = itemgetter('tweet_volume'), reverse = True)

topics = {}
for t in nyc_trends_list:
    topics[t['name']] = t['tweet_volume']

wordcloud = WordCloud(
    width = 1600,
    height = 900,
    prefer_horizontal = 0.5,
    min_font_size = 10,
    colormap = 'prism',
    background_color = 'white'
)

wc = wordcloud.fit_words(topics)
wc = wordcloud.to_file('TrendingTwitter_fall2020.png')