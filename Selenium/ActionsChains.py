import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
actions = ActionChains(driver)

driver.get("https://magento.softwaretestingboard.com/")
driver.maximize_window()

# Mouse Hover

women = driver.find_element(By.XPATH, "//a[@id='ui-id-4']")

actions.move_to_element(women).perform()

# move on Tops
tops = driver.find_element(By.XPATH, "//a[@id='ui-id-9']")
actions.move_to_element(tops).perform()

# click on Jackets
jackets = driver.find_element(By.XPATH, "//a[@id='ui-id-11']")
actions.click(jackets).perform()

time.sleep(2)

# keys actions --> Shift + "Test" + Enter

search = driver.find_element(By.ID, "search")
actions.click(search).key_down(Keys.SHIFT).send_keys("Test").key_up(Keys.SHIFT).key_down(Keys.ENTER).perform()

time.sleep(2)
driver.quit()