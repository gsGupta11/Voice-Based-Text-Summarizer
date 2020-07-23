import time
from selenium import webdriver
import mail
import scrapper
import text2voice
import voice2text
driver = webdriver.Firefox()


while True:
    topic = "pokemon"
    driver.get("https://en.wikipedia.org/wiki/"+topic)
    driver.maximize_window()
    scrapper.scrapepara(driver)