from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/")
driver.implicitly_wait(2)
driver.maximize_window()

driver.find_element(By.ID, "email").send_keys("Test@gmail.com")
driver.find_element(By.ID, "enterimg").click()

# Wait Sleep
# time.sleep(2) # python default sleep

# Implicit wait - Implicitly waiting, webdriver polls the dom webpage
# where web ui is not present immediately, it will wait for the element to be present in the dom webpage
# driver.implicitly_wait(5)

# Explicit wait - Allow your code to halt the execution or freeze the thread
# until the expected condition is met or the maximum time has elapsed
# to use it first call the WebDriverWait as variable and pass the driver and time in seconds

wait = WebDriverWait(driver, 5)
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))).send_keys("Vinay")
time.sleep(1)

driver.quit()