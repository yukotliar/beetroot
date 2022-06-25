# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/.
# As a result, store all comments in chronological order in JSON and dump it to a file.
# For this task use Threads for making requests to reddit API.

import json

import threading

import requests

def get_comments(value):
    print(threading.current_thread().name, 'Starting')
    response = requests.get(f"https://api.pushshift.io/reddit/search/comment/?q={value}&sort=desc&sort_type=created_utc")
    comments = response.json()
    json_name = value+".json"
    with open(json_name, "w") as outfile:
        json.dump(comments, outfile, indent=4)
    print(threading.current_thread().name, 'Exiting')

c1 = threading.Thread(name='comments1', target=get_comments('cats'))
c2 = threading.Thread(name='comments2', target=get_comments('dogs'))
c3 = threading.Thread(name='comments3', target=get_comments('mems'))

c1.start()
c2.start()
c3.start()