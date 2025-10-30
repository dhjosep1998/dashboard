import time
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")

def browser():
    chrome_path = r"C:\PROJETO EDILSON\dash\chrome-win64\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_path
    driver = webdriver.Chrome(options=chrome_options)

    yield driver
    driver.quit()
