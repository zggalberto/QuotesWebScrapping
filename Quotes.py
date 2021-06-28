import requests
from bs4 import BeautifulSoup

# Get page
URL='https://www.frasess.net/frases-de-la-vida-cortas-para-reflexionar-1.html'
page = requests.get(URL)

#Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

#Find all div elements with class="quote_text"
quotes = soup.find_all("div",class_="quote_text")

#for each element extract text and auhtor"
for quote in quotes:
    message=quote.find(text=True,recursive=False)
    author=quote.find("div",class_="quote_author")
    print("Quote="+message.strip())
    if author :
        print("Author="+author.text.strip())
