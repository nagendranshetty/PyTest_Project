from Locators.loginPgaeLocators import LoginPageLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = LoginPageLocators.username_textbox_id
        self.password_textbox_id = LoginPageLocators.password_textbox_id
        self.login_button_id = LoginPageLocators.login_button_id
        self.inValid_credentials_msg =LoginPageLocators.inValid_credentials_msg

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def check_inValidCredentials(self):
        msg = self.driver.find_element_by_id(self.inValid_credentials_msg).text
        return msg


