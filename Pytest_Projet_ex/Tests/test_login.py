# from PytestProject.POM.loginPage import LoginPage
# from PytestProject.POM.homePage import HomePage
from selenium import webdriver
import pytest
import time

class TestLogin():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="E:/Python Selenium Projects/Pytest_Projet_ex/Drivers/chromedriver.exe")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get("https://opensource-demo.orangehrmlive.com/")
        yield
        driver.close()
        driver.quit()
        # print("Test completed")

    def test_loginTestCase(self, test_setup):
        driver.find_element_by_id("txtUsername").send_keys("Admin")
        driver.find_element_by_id("txtPassword").send_keys("admin123")
        driver.find_element_by_id("btnLogin").click()
        time.sleep(5)
        title = driver.title
        assert title == "OrangeHRM"

    # def test_loginTestCase(self, test_setup):
    #     lPage = LoginPage(driver)
    #     lPage.enter_username("Admin")
    #     lPage.enter_password("admin123")
    #     lPage.clickLoginButton()
    #     time.sleep(3)
    #
    #     hPage = HomePage(driver)
    #     hPage.click_Welocme_dropDown()
    #     hPage.clickOnLogout()
    #     title = driver.title
    #     assert title == "OrangeHRM"

    # def test_teardown():
    #     driver.close()
    #     driver.quit()
    #     print("Test completed")



