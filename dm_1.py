import keys
import tweepy as t

auth = t.OAuthHandler(keys.api_key, keys.api_secret)

auth.set_access_token(keys.access_token, keys.secret_token)

api = t.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.get_user("prattprattpratt")
'''
print(user.name)
print(user.description)
print(user.status.text)
print(user.followers_count)
print(user.geo_enabled)
'''
me = api.me
#print(me.name)

followers = []

#print(user)

cursor = t.Cursor(api.followers, screen_name = 'prattprattpratt')

for account in cursor.items(10):
    followers.append(account.screen_name)

print(followers)

friends = []

cursor = t.Cursor(api.friends, screen_name = 'prattprattpratt')

for friend in cursor.items(10):
    friends.append(friend.screen_name)

print(friends)

#get user's recent tweets

chris_tweets = api.user_timeline(screen_name = 'prattprattpratt', count = 5)

#for tweet in chris_tweets:
    #print(f'{tweet.user.screen_name}: {tweet.text}\n')

mytweets = api.home_timeline()

for tweet in mytweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')