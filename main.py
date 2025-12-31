import requests
from datetime import date
from send_email import send_email

api_key = "70b082610d984c5d8679351192d366b5"
today = date.today()

topic = "tesla"

url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey=70b082610d984c5d8679351192d366b5&language=en"

# make a request 
request = requests.get(url)
content = request.json()

body = ""

for article in content["articles"][:20]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"
    
body = body.encode("utf-8")
send_email(message=body)