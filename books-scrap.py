
import requests
from bs4 import BeautifulSoup

# Sending a GET request to the website
scrap_books = requests.get('http://books.toscrape.com/')

# Check if the request was successful
if scrap_books.status_code == 200:
    # Parsing the HTML content of the page
    soup = BeautifulSoup(scrap_books.content, 'html.parser')
    
    # Getting the title of the page
    print(soup.title.string)
    
    # Find all book containers
    books = soup.find_all('article', class_='product_pod')
    
    # Extract and print the title, price, and availability of each book
    for book in books:
        title = book.h3.a['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        print(f'Title: {title}\nPrice: {price}\nAvailability: {availability}\n')
else:
    print(f"Failed to retrieve the page. Status code: {scrap_books.status_code}")
