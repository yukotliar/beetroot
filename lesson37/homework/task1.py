# Download and save to file robots.txt from wikipedia, twitter websites etc.
import requests
response = requests.get("https://en.wikipedia.org/robots.txt")
robots_text = response.text
print(robots_text)