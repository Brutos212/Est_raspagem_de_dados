import requests


res = requests.get("https://automatetheboringstuff.com/files/rj.txt")

# Baixando informações em txt por partes 
try:
    res.raise_for_status()
    file = open("RomeuEJulienta.txt", "wb")

    for chunk in res.iter_content(10000):
        file.write(chunk)
except Exception as exc:
    print("Houve um erro: %s" % (str))





#Se as informação no link estiver errado ele irá informar
#try:
#    res.raise_for_status()
#except Exception as exc:
#    print("Houve um erro: %s" % (exc))




#res = requests.get("https://www.amazon.com.br/s?k=python3&__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_1")

#if(res.status_code == requests.codes.ok):
#    print("Tamanho do arquivo: " + str(len(res.text)))
#    print("Conteúdo do arquivo: " + res.text)

#else:
#    print("Erro: " + str(res.status_code))
    


