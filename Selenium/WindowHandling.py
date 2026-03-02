from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Windows.html")
driver.maximize_window()

# Parent Window
parent = driver.current_window_handle  # Get the current window handle guid
print("parent window handler: ", parent)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()
# All Window
windows = driver.window_handles

# Switch to child window
for win in windows:
    print(win)
    if win != parent:
        driver.switch_to.window(win)

# do action in child window
driver.find_element(By.XPATH, "//span[text()='Downloads']").click()
time.sleep(3)

# Close the current window
driver.close()

# Switch to parent window
driver.switch_to.window(parent)

driver.find_element(By.XPATH, "//a[@href='http://www.selenium.dev']").click()

# Close all the windows
driver.quit()