import requests
import bs4


res = requests.get('https://medium.com/@digitalgiraffes/7-awesome-and-free-ai-tools-you-should-know-43a1630ea409') 
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
paragrahs = noStarchSoup.select('p')[-1]
print(paragrahs)