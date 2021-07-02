import requests
from bs4 import BeautifulSoup
#647 29/06/2021
# Get page
print("número de páginas a revisar: ")
n=input()
lista=list()
pagina=list()
tupla=tuple()
for x in range (int(n)):
    print("Revisando pagina: "+ str(x+1))
    URL='https://www.frasess.net/frases-de-la-vida-cortas-para-reflexionar-'+str(x+1)+'.html'
    page = requests.get(URL)

    #Parse the page
    soup = BeautifulSoup(page.content, 'html.parser')

    #Find all div elements with class="quote_text"
    quotes = soup.find_all("div",class_="quote_text")

    #for each element extract text and auhtor"
    for quote in quotes:
        message=quote.find(text=True,recursive=False)
        author=quote.find("div",class_="quote_author")
        #print("Quote="+message.strip())
        if not author :
            author="Anónimo"
            #print("Author="+author.text.strip())
        tupla=message,author
        pagina.append(tupla)
        print(tupla)
    lista.append(pagina)


    




