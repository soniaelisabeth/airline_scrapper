from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Lib():
    WEBDRIVER_PATH = '.\\tools\\chromedriver.exe'
    __MAP_ELEMENT = (By.ID, 'seat_map')

    def __init__(self):...

    def start_browser(self):
        self.driver = webdriver.Chrome(self.WEBDRIVER_PATH)
        return self.driver
    
    def wait_page(self, wait=5):
        if WebDriverWait(self.driver, wait).until(EC.presence_of_element_located(self.__MAP_ELEMENT)):
            return True

    def click(self, elem):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(elem)).click()