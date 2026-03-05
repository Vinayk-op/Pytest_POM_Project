from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

# Switching to frames window
# Using Index
# driver.switch_to.frame(0)   # if there is only one iframe in page then considerable to use index

# Using name or id
driver.switch_to.frame("singleframe") # using id
# driver.switch_to.frame("SingleFrame") # using name

# Using web element
# find the frame element using xpath
# frame_element = driver.find_element(By.XPATH, "//*[@id='Single']//iframe")
# driver.switch_to.frame(frame_element)

# Intract with element under iframe
input_box = driver.find_element(By.TAG_NAME, "input") # bcs only one input tag in entire html body
input_box.send_keys("This is input text box under frame")

# Return to home default
driver.switch_to.default_content()

driver.quit()

