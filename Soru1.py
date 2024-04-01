from bs4 import BeautifulSoup as bs
import requests
#  9780807047408 white fragility isbn
"""
isbn = input("ISBN num girin: ")
URL = 'https://www.amazon.com/s?k={isbn}'
URL = 'https://www.amazon.com/s?k={9780807047408}'
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36'}

sayfa = requests.get(URL, headers=headers)
soup = bs(sayfa.content,'xml.parser')
fiyatlar = soup.find_all('span', {'class':'a-price-whole'})
yazar=soup.find_all('div',{'class': 'a-row'})
#print(fiyatlar)
print(yazar)
"""

# ISBN numarasını kullanarak kitap bilgilerini alın
isbn=input("ISBN numaras girin:")

url = f'https://www.amazon.com/s?k={isbn}'
    
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    
    
response = requests.get(url, headers=headers)
    
soup = bs(response.text, 'lxml')
            # Kitap başlığını alma
title_element = soup.find('span', {'class': 'a-size-medium'})
title = title_element.text.strip() if title_element else "Bilgi Bulunamadı"
            # Yazar bilgisini alma
author_element = soup.find('div', {'class': 'a-row'})
author = author_element.text.strip() if author_element else "Bilgi Bulunamadı"
            # Fiyat bilgisini alma
price_element = soup.find('span', {'class': 'a-price'})
price = price_element.text.strip() if price_element else "Bilgi Bulunamadı"

            # XML formatında bilgileri oluşturma
xml_data = f"<book><title>{title}</title>\n<author>{author}</author>\n<price>{price}</price></book>"
    
print(xml_data)
