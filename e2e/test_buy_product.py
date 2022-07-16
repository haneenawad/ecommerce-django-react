import time

import pytest

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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
        # chrome_options.add_argument("--headless")  # browser doesnt open when run the test
        # chrome_options.add_argument("--disable-gpu")  # kartes msa5

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


def test_buy_product_without_account(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong").click()
    # driver.execute_script("window.scrollTo(0,247)")
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    assert driver.current_url == "http://127.0.0.1:8000/#/login?redirect=shipping"


def test_buy_product_with_account_after_logged_in(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("haneen.tester@gmail.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("Hha12345")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong").click()
    # driver.execute_script("window.scrollTo(0,247)")
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    driver.find_element(By.CSS_SELECTOR, ".w-100").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".justify-content-md-center").click()
    driver.find_element(By.ID, "address").click()
    driver.find_element(By.ID, "address").send_keys("Nazareth")
    driver.find_element(By.ID, "city").click()
    driver.find_element(By.ID, "city").send_keys("Nazareth")
    # driver.find_element(By.ID, "postalCode").click()
    # driver.find_element(By.ID, "postalCode").click()
    driver.find_element(By.ID, "postalCode").click()
    element = driver.find_element(By.ID, "postalCode")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.ID, "postalCode").send_keys("16000")
    driver.find_element(By.ID, "country").click()
    # driver.find_element(By.ID, "country").click()
    # element = driver.find_element(By.ID, "country")
    # actions = ActionChains(driver)
    # actions.double_click(element).perform()
    # driver.find_element(By.ID, "country").click()
    driver.find_element(By.ID, "country").send_keys("Israel")
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div > div > form > button').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
    # driver.find_element(By.CSS_SELECTOR, ".my-3").click()
    driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > form > button").click()
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div.row > div.col-md-4 > div > div > div:nth-child(7) > button").click()
    time.sleep(2)
    order_name = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > h1")

    assert order_name.is_displayed()


def test_buy_product_changing_total_price_with_changing_quantity(driver):
    driver.get("http://127.0.0.1:8000/#/")
    driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
    driver.find_element(By.ID, "email").click()
    driver.find_element(By.ID, "email").send_keys("haneen.tester@gmail.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("Hha12345")
    driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div:nth-child(3) > div > div:nth-child(1) > div > div > a > div > strong").click()
    # driver.execute_script("window.scrollTo(0,247)")
    time.sleep(1)
    driver.execute_script(
        "document.querySelector('#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button').scrollIntoView();")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,
                        "#root > div > main > div > div > div:nth-child(1) > div.col > div > div > div:nth-child(4) > button").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control").click()
    dropdown = driver.find_element(By.CSS_SELECTOR, ".col-md-3 > .form-control")
    dropdown.find_element(By.XPATH, "//option[. = '2']").click()
    price_for_one_string = driver.find_element(By.CSS_SELECTOR,
                                               "#root > div > main > div > div.col-md-8 > div > div > div > div:nth-child(3)").text
    price_for_one = float(price_for_one_string[1:])
    time.sleep(3)
    total_price_string = driver.find_element(By.CSS_SELECTOR,
                                             "#root > div > main > div > div.col-md-4 > div > div.list-group.list-group-flush > div").text
    total_price = float(total_price_string[-7:])

    assert total_price == (2 * price_for_one)
