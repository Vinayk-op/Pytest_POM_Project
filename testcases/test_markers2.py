import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

@pytest.mark.sanity
def test_markers2():
    print("This is test_markers2")
    assert True

@pytest.mark.login
def test_login_google():
    driver.get('https://www.google.com/')
    driver.quit()