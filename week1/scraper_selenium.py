import time 
from selenium import webdriver 
from selenium.webdriver import ChromeOptions
from IPython.display import Markdown, display 

options = ChromeOptions()
options.add_argument("--headless = new")

driver = webdriver.Chrome(options=options)
driver.get("https://openai.com/")
time.sleep(5)
display(Markdown(driver.page_source))
driver.quit()