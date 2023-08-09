from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

link = "https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

for elem in range(17):
        element_by_ros = WebDriverWait(browser, 10).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "ul[class*=categories-filter__main]>li")))
        element_by_ros[elem].click()
        time.sleep(3)
        browser.back()

try:
    element_by_ros = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, 'ul[class*=categories-filter__main]>li')))
    element_by_ros.click()
except TimeoutException:
    print("Timed out waiting for element to appear")