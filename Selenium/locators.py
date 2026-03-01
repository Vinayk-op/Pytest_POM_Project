from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
driver.get("https://www.incometax.gov.in/iec/foportal/")
driver.maximize_window()

"""locators = {    
id
name
class_name
tag_name
link_text
partial_link_text
css_selector
xpath
}
"""
e_verify_ele = driver.find_element(By.LINK_TEXT, "e- Verify Return")
e_verify_ele.click()

driver.find_element(By.LINK_TEXT, "Home").click()

partial_link_text_ele = driver.find_element(By.PARTIAL_LINK_TEXT, "PAN Status")
partial_link_text_ele.click()

"""
XPaths = {
# text
//tagname[text()='full name* ']

# contains --> partial text
//tagname[contains(text(),'partial full name']

# index
//tagname[1]

# OR & AND
//*[@id='xyz' and @class='abx']

# parent - child - ancestor

//form[@id='abc']/child::div
//form[@id='abc']/parent::form

//form[@id='abc']/ancestor::form]

# following - sibling - preceding
//input[@id='abc']//following-sibling::input
}
"""

driver.quit()
