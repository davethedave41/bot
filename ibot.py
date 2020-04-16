from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import os
import time

class IG_bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.base_url = 'https://www.instagram.com'
        self.login(self.username,self.password)
    def login(self, username, password):
        self.driver.get('{}/accounts/login/'.format(self.base_url))
        enter_username = WebDriverWait(self.driver,20).until(expected_conditions.presence_of_element_located((By.NAME, 'username')))
        enter_username.send_keys(self.username)
        enter_password = WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_element_located((By.NAME, 'password')))
        enter_password.send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(), 'Log In')]")[0].click()
        if self.driver.contains()
        time.sleep(1.5)

    def navigate_users(self, user):
        self.driver.get('{0}/{1}/'.format(self.base_url,user))

    def message_spam(self):
        self.driver.find_elements_by_xpath("//button[contains(text(), 'Message')]")[0].click()

if __name__ == '__main__':
    ig_bot = IG_bot('tu','tp')
    print(ig_bot.username)
    ig_bot.navigate_users('johannes_ritter')
    ig_bot.message_spam()
