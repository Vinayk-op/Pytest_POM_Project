from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# Dropdown handling with Select tag

# Select class declaration with web element
select_web_element = driver.find_element(By.ID, "Skills")

sel = Select(select_web_element)

# Select By Index
sel.select_by_index(3)

# select by value
sel.select_by_value('Configuration')

# select by visible text
sel.select_by_visible_text('Design')

# Current URL
print(driver.current_url)

# navigate to different url
driver.get("https://google.com")

# back
driver.back()

# refresh browser
driver.refresh()

# go forward tab
driver.forward()
print(driver.current_url)

driver.quit()