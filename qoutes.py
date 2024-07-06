import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'http://quotes.toscrape.com/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all quote containers
    quotes = soup.find_all('div', class_='quote')
    
    # Print all quotes
    print("All quotes on the page:")
    for quote in quotes:
        text = quote.find('span', class_='text').text
        author = quote.find('small', class_='author').text
        print(f'"{text}" - {author}')
    
    
    # Define the author to search for
    specific_author = 'Jane Austen'
    
    # Initialize a flag to check if a quote was found
    found_quote = False
    
    # Find and print the quote by the specific author
    for quote in quotes:
        author = quote.find('small', class_='author').text
        if author == specific_author:
            text = quote.find('span', class_='text').text
            print(f'Specific quote by {specific_author}:')
            print(f'"{text}" - {author}')
            found_quote = True
            break  # Stop after finding the first matching quote
    
    # If no quote was found by the specific author, print a message
    if not found_quote:
        print(f"No quotes found by {specific_author}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")

     