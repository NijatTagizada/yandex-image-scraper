from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pathlib import Path

path = 'driver/chromedriver'
driver_folder = Path(path)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(driver_folder.absolute(), options=chrome_options)
