import requests
from datetime import date

api_key = "70b082610d984c5d8679351192d366b5"
today = date.today()

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=70b082610d984c5d8679351192d366b5"

# make a request 
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])