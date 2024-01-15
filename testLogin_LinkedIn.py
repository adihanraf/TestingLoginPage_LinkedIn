import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(1)
    driver.maximize_window()
    yield driver
    driver.quit()

# @pytest.mark.parametrize("input1, input2",[("testlogin968@gmail.com", "Dihanrafiq25")])

## Login Berhasi
def test_login(driver):
    driver.get("https://linkedin.com/login")
    Email = driver.find_element(By.ID, "username")
    Password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")

    Email.send_keys("testlogin968@gmail.com")
    Password.send_keys("Dihanrafiq25")
    button.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Halaman Utama" in driver.page_source

## Login gagal, salah password (pesan error,Wrong email or password)
def test_failLogin(driver):
    driver.get("https://linkedin.com/login")
    Email = driver.find_element(By.ID, "username")
    Password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")

    Email.send_keys("testlogin968@gmail.com")
    Password.send_keys("Dihanrafiq22")
    button.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Wrong email or password." in driver.page_source

## Login gagal, Username & Password kosong (pesan error, Please enter an email address or phone number)
def test_emptyinput(driver):
    driver.get("https://linkedin.com/login")
    Email = driver.find_element(By.ID, "username")
    Password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.CSS_SELECTOR, "#organic-div > form > div.login__form_action_container > button")

    Email.send_keys("")
    Password.send_keys("")
    button.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Please enter an email address or phone number" in driver.page_source



