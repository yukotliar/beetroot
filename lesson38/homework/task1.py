import requests
from bs4 import BeautifulSoup

URL = "https://remote.co/remote-jobs/developer/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="card bg-white m-0")
job_elements = results.find_all("div", class_="card-body px-3 py-0 pl-md-0")
# print(results)
for job_element in job_elements:
    title_element = job_element.find("span", class_="font-weight-bold larger")
    title_element = title_element.text.strip()
    if "Senior" and "React" in title_element:
        print(title_element)
