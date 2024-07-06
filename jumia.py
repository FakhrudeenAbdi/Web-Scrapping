import requests
from bs4 import BeautifulSoup
import csv
#Fetches the content of a web page.

def get_page_content(url):
    """Fetches the content of the web page."""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve the web page. Status code: {response.status_code}")
        return None
#Extracts product details from an HTML element representing a product.
def parse_product_info(product):
    """Parses the product information from a product card."""
    product_name = product.find('h3', class_='name').text.strip()
    brand_name = product.find('div', class_='brand').text.strip() if product.find('div', class_='brand') else 'Infinix'
    price = product.find('div', class_='prc').text.strip()
    discount = product.find('div', class_='bdg _dsct _sm')
    discount = discount.text.strip().replace('%', '') if discount else '0'
    reviews = product.find('div', class_='rev')
    reviews = reviews.text.strip().split(' ')[0] if reviews else '0'
    rating = product.find('div', class_='stars _s')
    rating = rating['data-rate'] if rating and 'data-rate' in rating.attrs else '0'
#Returns: A dictionary containing the extracted product details.
    return {
        'Product Name': product_name,
        'Brand Name': brand_name,
        'Price (Ksh)': price,
        'Discount (%)': discount,
        'Total Number of Reviews': reviews,
        'Product Rating': rating
    }
#Scrapes product data from Jumia's Infinix Official Store.

def scrape_jumia_deals(url):
    """Scrapes product data from Jumia's Infinix Official Store."""
    page_content = get_page_content(url)
    if not page_content:
        return []

    soup = BeautifulSoup(page_content, 'html.parser')
    product_list = soup.find_all('article', class_='prd _fb col c-prd')

    products_data = []
    for product in product_list:
        product_info = parse_product_info(product)
        products_data.append(product_info)
    
    return products_data

#Saves the list of products to a CSV file.
def save_to_csv(products, filename):
    """Saves the list of products to a CSV file."""
    keys = products[0].keys() if products else []
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(products)

def main():
    url = "https://www.jumia.co.ke/mlp-anniversary/"
    products = scrape_jumia_deals(url)
    if products:
        save_to_csv(products, 'jumia_infinix_official_store.csv')
        print("Data saved to jumia_infinix_official_store.csv")
    else:
        print("No data scraped.")

if __name__ == "__main__":
    main()
