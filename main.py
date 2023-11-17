import requests
from bs4 import BeautifulSoup


url="https://blog.skillfactory.ru/top-29-bibliotek-dlya-python-chem-polzuyutsya-razrabotchiki/"
page=requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")


name=soup.find('h1')

for item in name:
    print(item.text)

avtor=soup.find('div',class_='banner__info-avtor')

try:
    for item in avtor:
        result_avtor = item.text
        print(result_avtor)
except:
    pass

images=soup.find_all('div',class_='block__history-img')

for image in images:
    src = image.find('img')['src']
    print(src)
try:
    for item in avtor:
        result_avtor = item.text
        print(result_avtor)
except:
    pass


podzherkhutui_text=soup.find_all("strong")
text=soup.find_all('p')
for item in text:
    print(item.text)

def remove_periods(text):
    return text.replace('.', '')

for item in podzherkhutui_text:
    modified_text = remove_periods(item.text)
    print(modified_text)

#<a href="https://blog.skillfactory.ru/experts/mariya-zharova/" class="internal-link">Мария Жарова</a>
#<div class="banner__info-avtor">
#<div class="block__history-img"> <div itemprop="image" itemscope="" itemtype="http://schema.org/ImageObject">
