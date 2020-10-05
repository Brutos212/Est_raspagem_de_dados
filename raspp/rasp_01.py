import requests, bs4

#res = requests.get("https://nostarch.com/")

try:
    arquvioDeExemplo = open('exemplo.html')
    #res.raise_for_status()
    #soup = BeautifulSoup(html, features="xml")
    #objectSoup = bs4.BeautifulSoup(res.text, features="lxml")
    objectSoup = bs4.BeautifulSoup(arquvioDeExemplo, features="lxml")
    listSpan = objectSoup.select('span')

    print(objectSoup)

    print(objectSoup)
    #listAuthor = objectSoup.select("#author")
    #listP = objectSoup.select('p')

    #print("Total de paragrafos:  " + str(len(listP)))
    #for eachP in listP:
        #print(eachP.getText())
        

    print("Total de autores: " + str(len(listAuthor)))
    print("Primeira tag: " + str(listAuthor[0]))
    print("Nome do primeiro autor: " + listAuthor[1].getText())

    #print("Segunda tag: " + str(listAuthor[1]))
    #print("Nome do segundo autor: " + listAuthor[1].get())
    

    print(res.text)
    print(listAuthor)
except Exception as exc:
    print('houve um erro: %s.' % (exc))
