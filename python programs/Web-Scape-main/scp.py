import requests
from bs4 import BeautifulSoup

# url things
url = 'https://www.formula1.com/en/results.html/2022/drivers.html'
info = requests.get(url)
html_info = info.content
soup = BeautifulSoup(html_info, 'html.parser')
print(soup, 'beautify')

para = soup.find_all('p')
all_para = set()
for link in para:
	if link.get('105') !='#':
		all_links.add(link.get('105'))
		print(all_links)
