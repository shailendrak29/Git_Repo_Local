import twitter
print ("Hello1")

module_contents = dir(twitter)
print(module_contents)

api = twitter.Api(
        consumer_key = "wHJMcAr1RIjtHGlCjtWnEaw6e",
        consumer_secret = "xUd9vd7kTiPdnkOOaVrYft9wkJ3Y9nhPt3bX9cZRDDSbsjOIDa",
        access_token = "76392233-7XPpAX1pY24hxq0gj6bWpaVDi6jg3Vpa1zUyYUwDr",
        access_secret = "sCTSY1NcIQDqMVHPcRtCS2m8z0KxUCxQIb8MRmYRqwXMk",
        bearer_token = "AAAAAAAAAAAAAAAAAAAAAFGEwAEAAAAAfwlY899mAik%2B9l3Xy1UTJFOPax4%3D8DKCK4L9AcTqqjGb4EIC8BrEaqlpb9OWtSK7yj4i1yU2WBweGI"
    )


#
# api_key = "wHJMcAr1RIjtHGlCjtWnEaw6e"
# api_key_secret = "xUd9vd7kTiPdnkOOaVrYft9wkJ3Y9nhPt3bX9cZRDDSbsjOIDa"
# access_token = "76392233-7XPpAX1pY24hxq0gj6bWpaVDi6jg3Vpa1zUyYUwDr"
# access_token_secret = "sCTSY1NcIQDqMVHPcRtCS2m8z0KxUCxQIb8MRmYRqwXMk"
# bearer_token = "AAAAAAAAAAAAAAAAAAAAAFGEwAEAAAAAfwlY899mAik%2B9l3Xy1UTJFOPax4%3D8DKCK4L9AcTqqjGb4EIC8BrEaqlpb9OWtSK7yj4i1yU2WBweGI"
#

t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

# client = tweepy.Client(bearer_token=bearer_token,
#                        consumer_key=api_key,
#                        consumer_secret=api_key_secret,
#                        access_token=access_token,
#                        access_token_secret=access_token_secret)
#
# # Get followers for a username
# username = "shailendra29"
# user = client.get_user(username=username)
#
# followers = client.get_users_followers(id=user.data.id, max_results=100)
#
# for follower in followers.data:
#     print(follower.username)