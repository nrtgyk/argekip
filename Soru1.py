from bs4 import BeautifulSoup as bs
import requests


#  9780807047408 white fragility isbn
"""
isbn = input("ISBN num girin: ")
URL = 'https://www.amazon.com/s?k={isbn}'

"""

# ISBN numarasını kullanarak kitap bilgilerini alın
isbn=input("ISBN numaras girin:")

url = f'https://www.amazon.com/s?k={isbn}'
    
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
    
    
response = requests.get(url, headers=header)
#if response.status_code != 200:
    #print(f"Error in getting webpage: {url}")
    
    
soup = bs(response.text, features='lxml')

first_product_tag = soup.find('div', {'class': 'a-product'})  # Örnek bir sınıf kullanıldı, gerçek HTML yapısına göre ayarlayın
    
    # İlk ürünün linkini bul
if first_product_tag:
    product_link = first_product_tag.find('a')['href']
        # Ürün linkini tam URL olarak oluştur
    product_url = f"https://www.amazon.com{product_link}"
    #yazar
    
    #fiyat
    price_element=soup.select_one('span',{'class':'a-size-base a-color-price a-color-price'})
    price = price_element.text if price_element else None
    #başlık
    title_element=soup.find('div',{'class':'a-section a-spacing-none a-text-center rpi-attribute-value rpi-iconic-attribute-text'})
    title=title_element.text if title_element else None
    
    #length
    length_element=soup.find('div',{'class':'a-section a-spacing-none a-text-center rpi-attribute-value rpi-iconic-attribute-text'})
    length=length_element.text if length_element else None
    
    
    #dil 
    language_element=soup.find('div',{'class':'a-section a-spacing-none a-text-center rpi-attribute-value rpi-iconic-attribute-text'})
    language=language_element.text if language_element else None
    
    #publisher
    publisher_element=soup.find()
    publisher=publisher_element.text if publisher_element else None
    
    #publication date
    publication_element=soup.find()
    publication=publication_element.text if publication_element else None
    #dimensions
    dimensions_element=soup.find()
    dimensions=dimensions_element.text if dimensions_element else None
    #ISBN-10
    isbn10_element=soup.find()
    isbn10=isbn10_element.text if isbn10_element else None
    #ISBN-13
    isbn13_element=soup.find()
    isbn13=isbn13_element.text if isbn13_element else None
    #images
    images_element= soup.find('div',{'class':'a-dynamic-image-container'})
    images=images_element.text if images_element else None
    
    #bookinfo
    bookinfo_element=soup.find()
    bookinfo=bookinfo_element.text if bookinfo_element else None
    
else:
     None
            
