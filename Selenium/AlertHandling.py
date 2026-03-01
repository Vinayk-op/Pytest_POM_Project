from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.maximize_window()


# Alert handling
driver.find_element(By.ID, 'OKTab').click()

time.sleep(2)

# OK ---> accept Alert
driver.switch_to.alert.accept()

time.sleep(2)

# alert with ok and cancel
driver.find_element(By.XPATH, "//a[@href='#CancelTab']").click()

driver.find_element(By.ID, 'CancelTab').click()
time.sleep(2)

driver.switch_to.alert.dismiss()
time.sleep(2)

# alert with text box
driver.find_element(By.XPATH, "//a[@href='#Textbox']").click()

driver.find_element(By.ID, 'Textbox').click()
time.sleep(2)

# get alert box text

alert_text = driver.switch_to.alert.text
print(alert_text)

# Enter into alert text box
driver.switch_to.alert.send_keys("Selenium Alert Handling")

driver.switch_to.alert.dismiss()

time.sleep(2)

driver.quit()