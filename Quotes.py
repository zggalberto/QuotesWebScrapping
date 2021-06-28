import requests
from bs4 import BeautifulSoup



URL='https://www.frasess.net/frases-de-la-vida-cortas-para-reflexionar-1.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

quotes = soup.find_all("div",class_="quote_text")


for quote in quotes:
    message=quote.find(text=True,recursive=False)
    author=quote.find("div",class_="quote_author")
    print("Quote="+message.strip())
    if author :
        print("Author="+author.text.strip())
