from urllib.request import urlopen
import numpy as np
import pandas as pd
url = 'https://www.imdb.com/title/tt0117060/reviews?ref_=tt_sa_3'
page = urlopen(url)
html_code = page.read().decode('utf-8')

from lxml import etree
a = []
tree = etree.HTML(html_code)
print(tree.xpath('//*[@id="main"]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]/text()')[0])
grade = int(tree.xpath('//*[@id="main"]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]/text()')[0])

df = pd.DataFrame(columns=['Name','URL','Mean','Max'])
df

url = 'https://www.imdb.com/title/tt13443470/reviews?ref_=tt_sa_3'
page = urlopen(url)
#print(page.read().decode('utf-8'))
html_code = page.read().decode('utf-8')

from urllib.request import urlopen
from lxml import etree
a = []
tree = etree.HTML(html_code)
print(tree.xpath('//*[@id="main"]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]/text()')[0])
grade = int(tree.xpath('//*[@id="main"]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]/text()')[0])

def midgrad(df,url):
    page = urlopen(url)
    html_code = page.read().decode('utf-8')
    a = []
    tree = etree.HTML(html_code)
    grade = int(tree.xpath('//*[@id="main"]/section/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/span/span[1]/text()')[0])
    c = '//*[@id="main"]/section/div[2]/div[2]/div[9]/div[1]/div[1]/div[1]/span/span[1]/text()'
    for i in range(9,19):
        d = i+1
        a +=(tree.xpath(c)[0])
        c = c.replace(str(i),str(d))
    for i in range(len(a)):
        a[i] = int(a[i])

    df1 = pd.DataFrame({'Name':[(tree.xpath('//*[@id="main"]/section/div[1]/div/div/h3/a/text()')[0])],'URL':[url],'Mean':[np.mean(a).round(2)], 'Max':[np.max(a)]})
    df = pd.concat([df, df1])
    return df

import numpy as np
films = np.array(['tt13443470', 'tt10048342', 'tt4912910', 'tt0120755', 'tt0458525', 'tt0120611', 'tt1745960', 'tt8574252'])

for i in films:
  url = 'https://www.imdb.com/title/'+i+'/reviews?ref_=tt_sa_3'
  df = midgrad(df, url)

df = df.reset_index(drop=True)
df

"""**2**"""

from bs4 import BeautifulSoup
import requests
url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops'
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
models = soup.find_all('a', class_='title')
description = soup.find_all('p', class_='description')
prices = soup.find_all('h4', class_='pull-right price')

with open('laptops.csv', 'w', encoding='utf-8') as file:
    file.write(f'Model;Desc;Price\n')
    for m, d, p in zip(models, description, prices):
        file.write(f"{m['title']};{d.get_text()};{p.get_text()}\n")

pd.read_csv('/content/laptops.csv',delimiter = ';')

"""**3**"""

df = pd.DataFrame(columns = ['Name','Author', 'Rating'])

df.loc[-1] = [1,2,3]

df

from bs4 import BeautifulSoup
import requests

df = pd.DataFrame(columns = ['Name','Author', 'Rating'])
url = 'https://www.livelib.ru/genre/%D0%A2%D1%80%D0%B8%D0%BB%D0%BB%D0%B5%D1%80%D1%8B/top'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content,'html.parser')
titles = soup.find_all('a', class_='brow-book-name with-cycle')
authors = soup.find_all('a', class_='brow-book-author')
rating = soup.find_all('span', class_='rating-value stars-color-orange')
i = 1
for t, a, r in zip(titles, authors, rating):
    df.loc[i] = [t.get_text(), a.get_text(), r.get_text()]
    i += 1

df

