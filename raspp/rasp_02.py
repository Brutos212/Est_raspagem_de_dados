import requests, webbrowser, bs4


print('Digite algo a ser buscado: ')
termosBuscados = input()

print("Buscando os termos: " + termosBuscados )

#Faz a requisição ao buscador de google
res = requests.get("https://www.google.com/search?q=" + termosBuscados)

#verifica se a reuisição foi bem sucedida
res.raise_for_status()

#bs4 analisa o html da página google retornada
parserSoup = bs4.BeautifulSoup(res.text, features="lxml")

#receber uma lista com os links das primeiras páginas retornadas da busca
linksList = parserSoup.select('.r, a')

#defino o numero de páginas que quero buscar
numeroDePaginasAbertas = 5

for i in range(numeroDePaginasAbertas):
    print("Abrindo página: https://www.google.com" + linksList[i].get('href') + "\n")
