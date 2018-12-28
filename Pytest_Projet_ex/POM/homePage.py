from Locators.homePgaeLocators import HomePageLocators

class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = HomePageLocators.welcome_link_id
        self.logout_link_text = HomePageLocators.logout_link_text

    def click_Welocme_dropDown(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def clickOnLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_text).click()

