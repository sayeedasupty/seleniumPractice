from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def login(username, password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
    time.sleep(2)
    return driver

def test_login_success():
    driver = login("Admin", "admin123")
    try:
        driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
        driver.find_element(By.LINK_TEXT, "Logout").click()
        print("Login Success Test Completed")
    except Exception as e:
        print("Login Success Test Failed:", e)
    finally:
        driver.close()
        driver.quit()

def test_login_wrong_password():
    driver = login("Admin", "wrongpassword")
    try:
        error_message = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
        if error_message == "Invalid credentials":
            print("Login Failed as expected. Error message:", error_message)
        else:
            print("Unexpected error message:", error_message)
    except Exception as e:
        print("Login Failure Test Failed:", e)
    finally:
        driver.close()

if __name__ == "__main__":
    test_login_success()
    test_login_wrong_password()