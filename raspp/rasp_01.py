import requests, bs4


try:
    # Importação relativa do arquivo exemplo.html da raíz do projeto.
    # Dependendo do SO, pode ser que tenha que remover o ../
    arquvioDeExemplo = open('../exemplo.html')
    objectSoup = bs4.BeautifulSoup(arquvioDeExemplo, features="lxml")
    
    # Exibição completa do HTML
    # print(objectSoup)
    
    listAuthor = objectSoup.select("#author")       

    print("Total de autores: " + str(len(listAuthor)))
    print("Primeira tag: " + str(listAuthor[0]))
    print("Nome do primeiro autor: " + listAuthor[1].getText())
        
except Exception as exc:
    print('houve um erro: %s.' % (exc))
