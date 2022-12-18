import requests
from bs4 import BeautifulSoup as bs
from googlesearch import search
from serpapi import GoogleSearch
from lxml import html


# web scrapping on any query the user enter and save each query result in a seprate text file

query = str(input('Enter your query search: '))
params = {
  "q": query,
  "hl": "en",
  "gl": "us",
  "google_domain": "google.com",
  "api_key": "enter your api key here"
}

# Function to remove tags
def remove_tags(html):
  
    # parse html content
    soup = bs(html, "html.parser")
  
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
urls = []

for result in organic_results:
    urls.append(result.get('link'))

contents = []
for url in urls:
    response = requests.get(url)
    clean_text = remove_tags(response.content)
    contents.append(clean_text)

for i in range(len(contents)):
    with open(f'result_{i}.txt','w+',encoding="utf-8") as f:
        f.write(contents[i])
        