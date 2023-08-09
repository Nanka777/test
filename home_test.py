import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link ="https://rozetka.com.ua/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(link)

search_string = browser.find_element(By.CSS_SELECTOR, "input[class*=search-form__input]")
search_string.send_keys("телефони")
button = browser.find_element(By.CSS_SELECTOR, "button[class*=button_color_green]")
button.click()
verification = browser.find_element(By.CSS_SELECTOR, "h1[class*=catalog-heading]").text
time.sleep(2)
verification_1 = "Мобільні телефони"
assert verification == verification_1, f"the test is not working, this is what you see - {verification}"
browser.quit()
