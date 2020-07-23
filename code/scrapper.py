from selenium import webdriver
import time

def scrapepara(driver):
    data =driver.find_element_by_tag_name("body")
    print(data.text)
