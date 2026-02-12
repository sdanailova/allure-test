import os
import allure
import pytest
from selenium import webdriver
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

    service = Service(executable_path=chromedriver_path) if chromedriver_path else Service()
    drv = webdriver.Chrome(service=service, options=options)
    yield drv
    drv.quit()


@allure.title("PASS: title should be HelloWorld Demo")
def test_title_pass(driver):
    driver.get(BASE_URL)
    assert driver.title == "HelloWorld Demo"


@allure.title("FAIL (intentional): heading text mismatch")
def test_heading_fail_intentional(driver):
    driver.get(BASE_URL)
    heading = driver.find_element(By.CSS_SELECTOR, "[data-testid='hero-title']").text
    assert heading == "HelloWorld!!!"  # intentional fail to show red test in Allure
