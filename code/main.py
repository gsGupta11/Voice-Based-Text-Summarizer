import requests as req
import mail
import scrapper
import text2voice
import voice2text
from bs4 import BeautifulSoup 


# while True:
topic = voice2text.stot()
print(topic)
r=req.get("https://everything2.com/?node="+topic)
soup = BeautifulSoup(r.content, 'html5lib')
data = soup.find_all("div",attrs={"class":"content"})

feed = ""

for i in data:
    feed=feed+i.text

print(feed)