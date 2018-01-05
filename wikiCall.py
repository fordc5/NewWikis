# Connor Ford
# Get new wikipedia pages


# Import the requests “The only Non-GMO HTTP library for Python, safe for human consumption.”
import requests

# For pretty printing of course!
from pprint import pprint

import datetime

def scrapeTweets():

    # Initialize new dictionary
    newdict = {}
         
    # Local to ISO-8601:
    dateStart = datetime.datetime.now().isoformat()[:-7] + 'Z'
    dateMinus1 = ((datetime.datetime.now() - datetime.timedelta(minutes=1)).isoformat())[:-7] + 'Z'
    #print(dateMinus1)
    
    # query the following from the wikipedia API:
    #  * new page creations
    #  * from last 1 seconds
    # return the following:
    #  * timestamp
    #  * title
    #  * flags
    requestURL = 'https://en.wikipedia.org/w/api.php?action=query&format=json&list=recentchanges&rcstart=' + dateStart + '&rcend=' + dateMinus1 + '&rcprop=title%7Cflags%7Ctimestamp%7Cuser&rctype=new&rclimit=max'
    r = requests.get(requestURL)
    
    # Get length of response
    # Make sure the request is not empty
    # Make sure new page is of correct format
    jsonResponse = r.json()
    jsonResponseLength = len(jsonResponse['query']['recentchanges'])
    if jsonResponseLength > 0:
        for newpage in jsonResponse['query']['recentchanges']:
            if not (newpage['title'].startswith("User talk:") or 
                 newpage['title'].startswith("Draft:") or 
                 newpage['title'].startswith("Talk:") or 
                 newpage['title'].startswith("User:") or
                 newpage['title'].startswith("Wikipedia:") or
                 newpage['title'].startswith("Template:") or
                 newpage['title'].startswith("Category:") or 
                 newpage['title'].startswith("Category talk:") ):
                newdict[newpage['title']] = newpage['user']
    if len(newdict) == 0:
        print("No new updates!")
    else:            
        print(newdict)
    
    # Print the json API response
    #pprint(r.json())
    
    return newdict
    