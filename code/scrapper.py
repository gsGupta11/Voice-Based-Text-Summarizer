from bs4 import BeautifulSoup
import requests as req

def get(topic):
    r=req.get("https://everything2.com/?node="+topic)
    soup = BeautifulSoup(r.content, 'html5lib')
    data = soup.find_all("div",attrs={"class":"content"})

    feed = ""
    for i in data:
        feed=feed+i.text
    return feed 