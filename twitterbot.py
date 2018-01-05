import tweepy
import time
import api_config as apiconfig
import wikiCall as wiki


starttime = time.time()

while True:

    consumer_key = apiconfig.api_config['CONSUMER_KEY']
    
    consumer_secret = apiconfig.api_config['CONSUMER_SECRET']
    
    access_token = apiconfig.api_config['ACCESS_TOKEN']
    
    access_token_secret = apiconfig.api_config['ACCESS_TOKEN_SECRET']
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    
    auth.set_access_token(access_token, access_token_secret)
    
    api = tweepy.API(auth)
    
    #####################################
    # Get user info
    #user = api.get_user('realDonaldTrump')
    #print("Name: ", user.name)
    #print("Location: ", user.location)
    #print("Following: ", user.friends_count)
    #print("Followers: ", user.followers_count)
    #####################################
    
    
    #####################################
    # SEND A TWEET
    tweetDict = wiki.scrapeTweets()
    
    if not len(tweetDict) == 0:
        
        for key, value in tweetDict.items():
    
            api.update_status(status= key.upper() + ": A new page is on Wikipedia! Created by " 
                              + value + ". Check it out here https://en.wikipedia.org/wiki/" + key.replace(' ', '_'))
            print("Tweet sent")
            
    #####################################
    
    
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))