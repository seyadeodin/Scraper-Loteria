from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://especiais.gazetadopovo.com.br/loterias/'

# cria uma conexão, salva a página
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# pareia código html
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll("div", {"class": "lista-concursos"})

# numbers = container.findAll("ul", {"class":"reset numbers_concurso"})

# cria arquivo csv contendo todos os dados
filename = "results.csv"
f = open(filename, "w")

headers = "mega, lotof, quina, time, dia, lotom\n"

f.write(headers)

for container in containers:
    print("Mega-Sena")
    for mega_container in container.findAll("li", {"class": "bg-mega-sena"}):
        mega = (mega_container.text)
        f.write(mega + " ")
        print(mega, end=' ')
    f.write(",")

    print("\nLoto-Fácil")
    for lotof_container in container.findAll("li", {"class": "bg-lotofacil"}):
        lotof = (lotof_container.text)
        f.write(lotof + " ")
        print(lotof, end=' ')
    f.write(",")

    print("\nQuina")
    for quina_container in container.findAll("li", {"class": "bg-quina"}):
        quina = (quina_container.text)
        f.write(quina + " ")
        print(quina, end=' ')
    f.write(",")

    print("\nTime-Mania")
    for time_container in container.findAll("li", {"class": "bg-timemania"}):
        time = (time_container.text)
        f.write(time + " ")
        print(time, end=' ')
    f.write(",")

    print("\nDia da Sorte:")
    for dia_container in container.findAll("li", {"class": "bg-diasorte"}):
        dia = (dia_container.text)
        f.write(dia + " ")
        print(dia, end=' ')
    f.write(",")

    print("\nLoto-Mania")
    for lotom_container in container.findAll("li", {"class": "bg-lotomania"}):
        lotom = (lotom_container.text)
        f.write(lotom + " ")
        print(lotom, end=' ')
    f.write(",")
    #f.write(mega + "," + lotof + "," + quina + "," + time + "," + dia + "," + lotom + "\n")

    f.close()
