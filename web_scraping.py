import requests
from bs4 import BeautifulSoup as soup

resp = requests.get("https://www.horoscopovirtual.com.br/horoscopo/libra")

html = soup(resp.text, 'html.parser')

hoje_div= html.find('div', attrs={'class': 'days-wrapper'})
hoje = hoje_div.find('p')
hoje = hoje.text

horoscopo_div = html.find('p', attrs={'class': 'text-pred'})
horoscopo = horoscopo_div.text.strip()

print(hoje, horoscopo)