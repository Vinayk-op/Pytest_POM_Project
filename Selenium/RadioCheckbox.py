from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# radio button handling

radio_female_btn = driver.find_element(By.XPATH, "//input[@value='FeMale']")
radio_female_btn.click()

radio_male_btn = driver.find_element(By.XPATH, "//input[@value='Male']")
radio_male_btn.click()

# Checkbox handling

checkbox_element_list = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for ele in checkbox_element_list:
    val = ele.get_attribute("value")
    print(val)
    if val =="Cricket":
        ele.click()