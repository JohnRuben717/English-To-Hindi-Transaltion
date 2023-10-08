from bs4 import BeautifulSoup

import requests

url = "https://karunya.edu"  # Replace with the URL of the webpage you want to scrape
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

text_content = soup.get_text()

print(text_content)
