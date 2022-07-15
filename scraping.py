from bs4 import BeautifulSoup
import requests

req =  requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(req.text,'html.parser')
link = soup.select('.titlelink')
score = soup.select('.score')
print(score[0])
