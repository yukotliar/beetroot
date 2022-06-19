# Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/
# As a result, store all comments in chronological order in JSON and dump it to a file.
import json

import requests

response = requests.get("https://api.pushshift.io/reddit/search/comment/?q=cats&sort=desc&sort_type=created_utc")
comments = response.json()
# print(comments)
with open("comments.json", "w") as outfile:
    json.dump(comments, outfile, indent=4)
