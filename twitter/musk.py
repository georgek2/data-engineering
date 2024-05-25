
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PATH = r'C:\Users\hp\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
# driver = webdriver.Chrome(PATH)

chrome_options = Options()
driver = webdriver.Chrome(options=chrome_options, keep_alive=True)
# Send a request using the webdriver
url = 'https://twitter.com/login'
driver.get(url)
















