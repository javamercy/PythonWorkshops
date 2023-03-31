from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.saucedemo.com/")
driver.maximize_window()


class TestSauce:
    def __init__(self) -> None:
        self.username = driver.find_element(By.ID, "user-name")
        self.password = driver.find_element(By.ID, "password")
        self.loginButton = driver.find_element(By.ID, "login-button")

    def username_and_password_empty(self):

        self.username.clear()
        self.password.clear()
        self.username.send_keys("")
        self.password.send_keys("")
        self.loginButton.click()
        sleep(2)
        iconForEmptyUsername = driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(1) > svg")
        iconForEmptyPassword = driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div:nth-child(2) > svg")
        print("icon for username: " + str(iconForEmptyUsername.is_displayed()))
        print("icon for password: " + str(iconForEmptyPassword.is_displayed()))
        errorText = driver.find_element(
            By.CSS_SELECTOR, "h3[data-test='error']").text
        print(errorText == "Epic sadface: Username is required")

        errorButton = driver.find_element(
            By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error > h3 > button")
        errorButton.click()
        sleep(2)
        print("icon for username: " + str(iconForEmptyUsername.is_displayed()))
        print("icon for password: " + str(iconForEmptyPassword.is_displayed()))

    def only_password_empty(self):
        self.username.clear()
        self.password.clear()
        self.username.send_keys("ahaha")
        self.password.send_keys("")
        self.loginButton.click()
        sleep(2)
        errorText = driver.find_element(
            By.CSS_SELECTOR, "h3[data-test='error']").text
        print(errorText == "Epic sadface: Password is required")

    def locked_out_user_login(self):
        self.username.clear()
        self.password.clear()
        self.username.send_keys("locked_out_user")
        self.password.send_keys("secret_sauce")
        self.loginButton.click()
        sleep(2)
        errorText = driver.find_element(
            By.CSS_SELECTOR, "h3[data-test='error']").text
        print(errorText == "Epic sadface: Sorry, this user has been locked out.")

    def standart_user_login(self):
        self.username.clear()
        self.password.clear()
        self.username.send_keys("standard_user")
        self.password.send_keys("secret_sauce")
        self.loginButton.click()
        sleep(2)
        print(driver.current_url == "https://www.saucedemo.com/inventory.html")
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(len(items) == 6)


testSauce = TestSauce()
# testSauce.usernameAndPasswordEmpty()
# testSauce.only_password_empty()
# testSauce.locked_out_user_login()
testSauce.standart_user_login()

while True:
    continue
