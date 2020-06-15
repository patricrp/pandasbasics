import tweepy
import json
import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
consumer_key = os.getenv("API_KEY")
consumer_secret = os.getenv("API_SECRET_KEY")
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

#Authentication process
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#Calling API. Setting notifications if reaching limit. Keep downloading when the window is available again.

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#Request tweets for a new search

def searchTweets(query, lang, geo):
    '''
    Perform a query search request to Twitter with Tweepy. Parameters:
    - query: include a word or a complex query using operators
    - lang: language ISO code 639-1
    - geo: latitude, longitude and km or miles
    
    Returns a dataframe with the columns: query, date, id, user and text.
    '''
    print('Creating an empty dataframe with the first 10 tweets')
    try:
        count = 0
        #First request
        while count < 1:
            tweets = tweepy.Cursor(api.search,
                               q=query,
                               lang=lang,
                               geo=geo,
                               result_type='mixed').items(10)


            data = [[query,tweet.created_at, tweet.id, tweet.user.screen_name, tweet.text] for tweet in tweets]

            df_tw = pd.DataFrame(data=data, columns=['query','date', 'id', 'user', 'tweet_text'])
            print('Here you have your first 10 tweets')
            print(df_tw)

            count += 1

        #Add more tweets
        while count >= 1:
            tweets = tweepy.Cursor(api.search,
                                       q=query,
                                       lang=lang,
                                       geo=geo,
                                       result_type='mixed',
                                       max_id=df_tw.id.min()).items(1500)


            data = [[query, tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text] for tweet in tweets]
            df2 = pd.DataFrame(data=data, columns=['query', 'id', 'date', 'user', 'tweet_text'])
            df_tw = df_tw.append(df2, sort=True)

            count += 1
            print('Adding 1500 to the dataframe')
            print('Your dataframe has a total of', df_tw.shape[0], 'tweets.')
            print('Oldest tweet is from', df_tw.date.min())

            return df_tw.to_csv('df_search.csv')
    except AttributeError:
        pass
    except NameError:
        pass

#Request tweets to update a dataframe
def updateTweets(query, lang, geo, df_tw):
    '''
    Perform a query search request to Twitter with Tweepy. Update the dataframe with the lastest tweets.
    Parameters:
    - query: include a word or a complex query using operators
    - lang: language ISO code 639-1
    - geo: latitude, longitude and km or miles
    - df_tw: dataframe to update. It should have the columns: query, date, id, user and text.
    
    Returns a dataframe with all the tweets. 
    '''
    if not df_tw.empty: 
        print('Dataframe is not empty')
        try:
            #Dataframe not empty, update tweets
            count = 1
            while count >= 1:
                tweets = tweepy.Cursor(api.search,
                                           q=query,
                                           lang=lang,
                                           geo=geo,
                                           result_type='mixed',
                                           since_id=df_tw.id.max()).items(1500)


                data = [[query, tweet.id, tweet.created_at, tweet.user.screen_name, tweet.text] for tweet in tweets]
                df2 = pd.DataFrame(data=data, columns=['query', 'id', 'date', 'user', 'tweet_text'])
                df_tw = df_tw.append(df2, sort=True)

                count += 1
                print('Updating your dataframe. Adding 1500 to the dataframe')
                print(df_tw.shape)
                print('Id max', df_tw.id.max())
                return df_tw.to_csv('df_search.csv')
        except AttributeError:
            pass
        except NameError:
            pass