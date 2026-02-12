import os
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:3000")


@pytest.fixture()
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    chrome_bin = os.getenv("CHROME_BIN")
    chromedriver_path = os.getenv("CHROMEDRIVER_PATH")

    if chrome_bin:
        options.binary_location = chrome_bin

    if chromedriver_path:
        service = Service(executable_path=chromedriver_path)
        drv = webdriver.Chrome(service=service, options=options)
    else:
        drv = webdriver.Chrome(options=options)

    yield drv
    drv.quit()


@allure.title("PASS: Page title should match")
def test_title_pass(driver):
    driver.get(BASE_URL)
    # From your logs, actual title is "HelloWorld Demo"
    assert driver.title == "HelloWorld Demo"


@allure.title("FAIL (intentional): Heading text mismatch")
def test_heading_fail_intentional(driver):
    driver.get(BASE_URL)
    heading = driver.find_element(By.CSS_SELECTOR, '[data-testid="hero-title"]').text
    # Keep this intentionally wrong to demonstrate failure in Allure
    assert heading == "This will fail on purpose"
