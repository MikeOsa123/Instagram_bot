from selenium import webdriver
import os
import time
from instagram_credentials import username, password

class InstagramBot:
    """
   Initializes an instance of the InstagramBot class. 
   
   Call the login method to authenciate the user to login
   
    Args:
        username:str: The Instagram username for a user
        password:str: The Instagram password for a user

    Attributes:
        driver:Selenium.webdriver.Chrome: The Chromedriver that is used to automate browser actions
    """
    def __init__(self, username, password):

        self.username = username
        self.password = password
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('chromedriver')

        self.login()

        

    def login(self):
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)

        time.sleep(1)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        time.sleep(1)

    def nav_user(self, user):
        self.driver.get('{}/{}/'.format(self.base_url, user))

    def follow_user(self, user):
        self.nav_user(user)

        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")

        follow_button[0].click()


if __name__ == '__main__':
    ig_bot = InstagramBot(username, password)

    # ig_bot.nav_user('mikeosa')
    ig_bot.follow_user('mikeosa')


