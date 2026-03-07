from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.redbus.in/")
driver.implicitly_wait(5)
driver.maximize_window()

select_date = "20-Feb-2023"

dates = select_date.split("-")

date_field = driver.find_element(By.XPATH, "//*[@data-autoid='searchWidget']//div[@class='dateWrapper___fc49bd ']")
date_field.click()

td = driver.find_elements(By.XPATH, "//div[@role='row']/li")

for ele in td:
    print(ele.text)
    if ele.text == dates[0]:
        ele.click()
        break     # bcs once clicked calender will be closed and we need to break the loop to avoid StaleElementReferenceException

