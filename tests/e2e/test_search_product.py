import time

import pytest

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    firefox_driver_binary = "geckodriver.exe"
    ser_firefox = FirefoxService(firefox_driver_binary)
    firefox_options = FireFoxOptions()
    chrome_options = ChromeOptions()

    browser_name = 'chrome'
    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        firefox_options.add_argument("--headless")  # with the browser doesnt open
        dc = {
            "browserName": "firefox",
            # "browserVersion": "101.0.1(x64)",
            "platformName": "Windows 10"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)

    elif browser_name == "chrome":
        chrome_options.add_argument("--headless")  # browser doesnt open when run the test
        chrome_options.add_argument("--disable-gpu")  # kartes msa5

        dc = {
            "browserName": "chrome",
            "platformName": "Windows 10"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)

    elif browser_name == "android-emulator":
        dc = {
            "platformName": "Android",
            "platformVersion": "8.1.0",
            "deviceName": "Android Emulator",
            # "platformVersion": "11.0.0",
            # "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            # "app": "com.android.chrome",
            "browserName": "Chrome"
        }
        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)

    elif browser_name == "android-phone":
        dc = {
            "platformName": "Android",
            "platformVersion": "11.0.0",
            "deviceName": "1aaa4ea80404",
            "automationName": "Appium",
            "browserName": "Chrome"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
    else:
        raise Exception("driver doesn't exists")
    yield driver
    driver.close()


def test_search_product(driver):
    driver.get("http://127.0.0.1:8000/#/")
    name_product = driver.find_element(By.CSS_SELECTOR,
                                       "#root > div > main > div > div:nth-child(3) > div > div:nth-child(3) > div > div > a > div > strong").text
    driver.find_element(By.NAME, "q").click()
    driver.find_element(By.NAME, "q").send_keys(name_product)
    driver.find_element(By.CSS_SELECTOR, ".p-2").click()
    time.sleep(2)
    searched_product = driver.find_element(By.CSS_SELECTOR,
                                           "#root > div > main > div > div > div > div:nth-child(1) > div > div > a > div > strong").text
    # assert searched_product == name_product
    assert searched_product == "hero"

