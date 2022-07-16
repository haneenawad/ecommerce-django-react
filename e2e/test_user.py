# import time
#
# import pytest
#
# from selenium import webdriver
# from selenium.webdriver import Keys
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options as FireFoxOptions
# from selenium.webdriver.firefox.service import Service as FirefoxService
#
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# @pytest.fixture()
# def driver():
#     firefox_driver_binary = "geckodriver.exe"
#     ser_firefox = FirefoxService(firefox_driver_binary)
#     firefox_options = FireFoxOptions()
#     chrome_options = ChromeOptions()
#
#     browser_name = 'chrome'
#     # if isinstance(browserName,list):
#     #     for browser_name in browserName:
#     if browser_name == "firefox-webdriver":
#         driver = webdriver.Firefox(service=ser_firefox)
#     elif browser_name == "firefox":
#         firefox_options.add_argument("--headless")  #with the browser doesnt open
#         dc = {
#             "browserName": "firefox",
#             # "browserVersion": "101.0.1(x64)",
#             "platformName": "Windows 10"
#         }
#         driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc, options=firefox_options)
#
#     elif browser_name == "chrome":
#         chrome_options.add_argument("--headless")  # browser doesnt open when run the test
#         chrome_options.add_argument("--disable-gpu")  # kartes msa5
#
#         dc = {
#             "browserName": "chrome",
#             "platformName": "Windows 10"
#         }
#         driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)
#
#     elif browser_name == "firefox-mobile":
#         firefox_options = FireFoxOptions()
#         firefox_options.add_argument("--width=375")
#         firefox_options.add_argument("--height=812")
#         firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
#                                                                      "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
#                                                                      "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
#         # firefox_options.set_preference("general.useragent.override", "Nexus 7")
#
#         driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)
#
#     elif browser_name == "android-emulator":
#         dc = {
#             "platformName": "Android",
#             "platformVersion": "8.1.0",
#             "deviceName": "Android Emulator",
#             # "platformVersion": "11.0.0",
#             # "deviceName": "1aaa4ea80404",
#             "automationName": "Appium",
#             # "app": "com.android.chrome",
#             "browserName": "Chrome"
#         }
#         driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
#
#     elif browser_name == "android-phone":
#         dc = {
#             "platformName": "Android",
#             "platformVersion": "11.0.0",
#             "deviceName": "1aaa4ea80404",
#             "automationName": "Appium",
#             "browserName": "Chrome"
#         }
#
#         driver = webdriver.Remote("http://localhost:4723/wd/hub", dc)
#     else:
#         raise Exception("driver doesn't exists")
#     yield driver
#     driver.close()
#
#
# '''
# testing user
#
# '''
#
#
# def test_user_login(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("haneen.tester@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     username = driver.find_element(By.CSS_SELECTOR, "#username").text
#     assert username == "TESTER"
#
#
# def test_user_create_account(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(5)
#     register.click()
#     time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("Awad")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("awad@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(4)
#     driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     # username = driver.find_element(By.CSS_SELECTOR, "#username").text
#     # assert username == "AWAD"
#
#
# def test_user_create_account_for_existed_account(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(3)
#     register.click()
#     # time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("Awad")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("awad@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     # driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     error_note = driver.find_element(By.CSS_SELECTOR,
#                                      "#root > div > main > div > div > div > div.fade.alert.alert-danger.show").text
#     assert error_note == "User with this email is already registered"
#
#
# def test_user_invalid_username(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("a@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div.fade.alert.alert-danger.show').scrollIntoView();")
#     error_note = driver.find_element(By.CSS_SELECTOR,
#                                      "#root > div > main > div > div > div > div.fade.alert.alert-danger.show").text
#     assert error_note == "No active account found with the given credentials"
#
#
# def test_user_incorrect_password(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("haneen.tester@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha1234")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div.fade.alert.alert-danger.show').scrollIntoView();")
#     error_note = driver.find_element(By.CSS_SELECTOR,
#                                      "#root > div > main > div > div > div > div.fade.alert.alert-danger.show").text
#     assert error_note == "No active account found with the given credentials"
#
#
# def test_user_create_account_with_incorrect_email_format(driver):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a"))).click()
#     driver.execute_script(
#         "document.querySelector('#root > div > main > div > div > div > div > div > a').scrollIntoView();")
#     register = driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > div > div > div > div > a")
#     time.sleep(3)
#     register.click()
#     # time.sleep(5)
#     driver.find_element(By.ID, "name").click()
#     driver.find_element(By.ID, "name").send_keys("awad")
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("a")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.ID, "passwordConfirm").click()
#     driver.find_element(By.ID, "passwordConfirm").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     # driver.execute_script("window.scrollTo(0,198.6666717529297)")
#     assert driver.current_url == "http://127.0.0.1:8000/#/register?redirect=/"
#
#
# '''
# testing admin user
#
# '''
#
#
# @pytest.mark.parametrize("validation", ["HANEEN", "ADMIN"])
# def test_admin_user_login(driver, validation):
#     driver.get("http://127.0.0.1:8000/#/")
#     driver.find_element(By.CSS_SELECTOR, ".nav-link:nth-child(2)").click()
#     # time.sleep(2)
#     driver.find_element(By.ID, "email").click()
#     driver.find_element(By.ID, "email").send_keys("haneen.awad@gmail.com")
#     driver.find_element(By.ID, "password").click()
#     driver.find_element(By.ID, "password").send_keys("Hha12345")
#     driver.find_element(By.CSS_SELECTOR, ".mt-3").click()
#     time.sleep(2)
#     username = driver.find_element(By.CSS_SELECTOR, "#username").text
#     admin = driver.find_element(By.CSS_SELECTOR, "#adminmenu").text
#     names = [username, admin]
#     assert validation in names
#
# #1
