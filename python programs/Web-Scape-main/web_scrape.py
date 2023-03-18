# importing all the shit
import requests
from bs4 import BeautifulSoup
import html5lib
# pip install pyperclip

# url
source = requests.get('https://www.formula1.com/en/results.html/2021/drivers.html').text
soup = BeautifulSoup(source, 'html.parser')
article = soup.find('article')
# print(article.prettify())
points = article.find(class_='resultsarchive-table').text
print(points)
