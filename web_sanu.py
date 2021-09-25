import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager

from selenium.common.exceptions import ElementClickInterceptedException

from selenium import webdriver 

driver = webdriver.Chrome(ChromeDriverManager().install())

search_url="https://www.google.com/search?q={q}&tbm=isch&tbs=sur%3Afc&hl=en&ved=0CAIQpwVqFwoTCKCa1c6s4-oCFQAAAAAdAAAAABAC&biw=1251&bih=568" 

# driver.get(search_url.format(q='Car'))
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver.get("https://www.imdb.com/india/top-rated-indian-movies/?ref_=nv_mv_250_in")
# print(driver.title)
# driver.quit()

# driver.get("https://www.w3schools.com/js/default.asp")
# print(driver.title)
# driver.quit()

driver.get("https://www.tutorialspoint.com/javascript/javascript_overview.htm")
print(driver.title)
driver.quit()


