from selenium.webdriver.common.by import By
from lib import Lib
import logging

class SeatsPage(Lib):
    __SEATS_TABLE = (By. ID)

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        page = self.driver.get(url)
        # self.wait_page(page)
        print('')

    def get_seats_map(self):
        self.click()
    
    def screenshot(self):
        ...
