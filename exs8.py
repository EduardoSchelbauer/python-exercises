import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
resposta = requests.get(url)

soup = BeautifulSoup(resposta.text)

titulos = soup.find_all('title').string

for titulo in titulos:
    print(titulo.text)