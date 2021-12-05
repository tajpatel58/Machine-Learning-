#%%
import requests 
from pprint import pprint 
import pandas as pd
import time 

# This is a task in using the stack exchange API to obtain the questions 
# with the most upvotes in the last 24 hours.  
answers_url = 'https://api.stackexchange.com/2.3/answers?page=https%3A%2F%2Fstackoverflow.com%2Fquestions%3Fsort%3DMostVotes%26edited%3Dtrue&fromdate=1633996800&todate=1634083200&order=desc&sort=votes&site=stackoverflow'

answers_url_2 = 'https://api.stackexchange.com/2.3/answers?fromdate=1633996800&todate=1634083200&order=desc&sort=votes&site=stackoverflow'

r = requests.get(answers_url_2)
print(r)

#%%

json_data = r.json()

list_questions = json_data['items']

x = list_questions[0]['score']

for dictionary in list_questions:
    print(dictionary['score'])


#pprint(list_questions)
#top_questions_json = json_data['items']

#up_votes = [question['score'] for question in top_questions_json]
# %%

# Now we try to get use the Stack API to obtain the first 3 badges(alphabetically).

badges_url = 'https://api.stackexchange.com/2.3/badges?pagesize=3&order=asc&sort=name&site=stackoverflow'

badges_request = requests.get(badges_url)

json_badges = badges_request.json()

pprint(json_badges)

# Now we want to use Stack API to get the most recent recipients of these badges

# First we need to extract the badge ID's:

list_badges = json_badges['items']

badges = [badge['badge_id'] for badge in list_badges]

users_badges = f'https://api.stackexchange.com/2.3/badges/9878;204;600/recipients?site=stackoverflow&pagesize=3'


badge_users = requests.get(users_badges).json()

pprint(badge_users)

# %%

# Pagination Task: Requesting the first 5 pages of questions from StackExchange.

def pagination(endpoint): 
    posts = [] 
    for j in range(1, endpoint+1):
        posts_data = requests.get(f'https://api.stackexchange.com/2.3/posts?page={j}&fromdate=1631577600&todate=1634169600&order=desc&sort=activity&site=stackoverflow')
        json_posts = posts_data.json()
        posts.append(json_posts)
    return posts 

pprint(pagination(5))


# %%
