import requests
from datetime import date
from send_email import send_email

api_key = "70b082610d984c5d8679351192d366b5"
today = date.today()

url = f"https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=70b082610d984c5d8679351192d366b5"

# make a request 
request = requests.get(url)
content = request.json()

email_body = ""

for article in content["articles"]:
    title = article["title"]
    description = article["description"]

    email_body += f"""

Title: {title}
Description: {description}

--------------------------
"""
    
send_email(email_body)