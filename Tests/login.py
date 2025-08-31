import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class LoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get("https://opensource-demo.orangehrmlive.com/")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def login(self, username, password):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(2)
        return self.driver

    def test_login_success(self):
        driver = self.login("Admin", "admin123")
        try:
            driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name").click()
            driver.find_element(By.LINK_TEXT, "Logout").click()
            print("Login Success Test Completed")
        except Exception as e:
            print("Login Success Test Failed:", e)

    def test_login_wrong_password(self):
        driver = self.login("Admin", "wrongpassword")
        try:
            error_message = driver.find_element(By.CLASS_NAME, "oxd-alert-content-text").text
            if error_message == "Invalid credentials":
                print("Login Failed as expected. Error message:", error_message)
            else:
                print("Unexpected error message:", error_message)
        except Exception as e:
            print("Login Wrong Password Test Failed:", e)

if __name__ == "__main__":
    unittest.main()