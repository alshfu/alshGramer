import selenium

from Actions.target_page.page_init import Page
from proffile import *
from settings import *
from selenium import webdriver


class Action():

    def __init__(self):
        self.user = User()
        self.settings = Settings()
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.url = self.settings.get_url()

    def login_to_instagram(self):
        self.settings.random_paus_interval(2, 3, "input userName")
        self.driver.find_element_by_name('username').send_keys(self.user.get_user_name())
        self.settings.random_paus_interval(2, 3, "input Password")
        self.driver.find_element_by_name('password').send_keys(self.user.get_user_password())
        self.settings.random_paus_interval(4, 7, "click on login button")
        self.driver.find_elements_by_tag_name('button')[1].click()

    def save_login_information(self, driver):
        self.settings.random_paus_interval(4, 7, "Answer for question about login ")
        driver.find_elements_by_tag_name('button')[0].click()

    def active_notifications(self, driver):
        self.settings.random_paus_interval(3, 5, "Answer for question about notifications")
        buttons = driver.find_elements_by_tag_name('button')
        for button in buttons:
            # TODO: создать параметры локализации
            if "Aktivera" in button.text:
                button.click()
                break

    def browser(self):
        driver = self.driver
        driver.get(self.url)
        self.settings.random_paus_interval(5, 7, "Open instagram")
        self.login_to_instagram()
        self.save_login_information(driver)
        self.active_notifications(driver)
        Page().open(driver)
        input("Close")
        driver.close()
        pass

