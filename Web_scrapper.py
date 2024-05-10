import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

# a request to the website
r = requests.get("http://books.toscrape.com")

# Create a BeautifulSoup object and specify the parser
soup = BeautifulSoup(r.text, 'html.parser')

# Extract the title of the page, meta description and url
page_title = soup.title.text
print("Page Title: ", page_title)

meta_description = soup.find('meta', attrs={'name': 'description'})
print("Meta Description: ", meta_description['content'] if meta_description else "Not available")

for link in soup.find_all('a'):
    url = link.get('href')
    
    # Convert the relative URL to an absolute URL
    absolute_url = urljoin("books.toscrape.com", url)
    print("URL: ", absolute_url)

    # Parse the URL to extract the file structure and directory
    parsed_url = urlparse(absolute_url)
    print("File Structure and Directory: ", parsed_url.path)