import os
import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from utilities import ReadConfigurations

@pytest.fixture()
def setup_and_teardown(request):
    options = Options()
    options.add_argument("--start-maximized")

    headless_flag = ReadConfigurations.read_configuration("basic info", "headless")
    if headless_flag.lower() == "yes" or os.getenv("CI", "false").lower() == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    if os.getenv("CI", "false").lower() == "true":
        # CI/CD → webdriver-manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        # Local → PATH driver
        driver = webdriver.Chrome(options=options)

    url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(url)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture()
def log_on_failure(request, setup_and_teardown):
    yield
    if request.node.rep_call.failed:
        allure.attach(setup_and_teardown.get_screenshot_as_png(),
                      name="failed_test",
                      attachment_type=AttachmentType.PNG)