from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://cnblogs.com/")
print(browser.current_url)

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)
