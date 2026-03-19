import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='module')
def launch_browser():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    driver.quit()

@pytest.fixture(scope='class')
def launch_class_browser(request):
    request.cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield
    request.cls.driver.quit()


def test_login_amaz(launch_browser):
    driver.get('https://www.amazon')

def test_get_title(launch_browser):
    print(driver.title)

@pytest.mark.usefixtures('launch_class_browser')
class Test_classFixture:
    def test_login_cls(self):
        self.driver.get("https://www.facebook.com/")
        print(self.driver.title)