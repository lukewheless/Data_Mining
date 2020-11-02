import keys 
import tweepy as t

a = t.OAuthHandler(keys.api, keys.secret)

a.set_access_token(keys.access_token, keys.access_secret)

api = t.API(a, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.get_user("wheeliefbaby")

print(user.name)
#print(user.description)
print(user.followers_count)


cursor = t.Cursor(api.followers, screen_name = "wheeliefbaby")
followers = []

for account in cursor.items(5):
    followers.append(friend.screen_name)

print(followers)

josh_tweets = api.user_timeline(screen_name= "wheeliefbaby", count = 5)

for tweet in josh_tweets:
    print(f'{tweet.user.screen_name}: {tweet.text}\n')



















