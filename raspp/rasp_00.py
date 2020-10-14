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
