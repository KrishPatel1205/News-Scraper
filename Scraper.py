from bs4 import BeautifulSoup
import requests


source = requests.get("https://inshorts.com/en/read").text

soup = BeautifulSoup(source, "lxml")

with open('news.txt', 'w', encoding='utf-8') as txt_file:
    for article in soup.find_all('div', class_='news-card z-depth-1'):
        headline = article.find('span', itemprop='headline').text
        summary = article.find('div', itemprop='articleBody').text

        txt_file.writelines(headline + "\n" + summary + "\n" + "\n")
        # print("\033[1m" + headline + "\033[0m" + "\n" + summary + "\n" + "\n")