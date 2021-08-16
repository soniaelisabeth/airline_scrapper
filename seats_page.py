from selenium.webdriver.common.by import By
from lib import Lib

class SeatsPage(Lib):
    __SEAT_BUTTON = By.ID, 'select-seat'
    __CONFIRM_BUTTON = By.ID, 'next-button'
    __GREEN_SEATS = '#AADB72'
    __BLUE_SEATS = '#9BC8E4'
    __EXIT_SEAT_BUTTON = By.ID, 'accept_exit_regulations'
    __SEAT_SELECTION_BOX = By.CLASS_NAME, 'sc-eCssSg'

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    def locate_seats(self, row, position):
        airplane_rows = self.driver.find_element_by_class_name(f'row-{row}')
        airplane_seats = airplane_rows.find_elements_by_tag_name('button')

        if not airplane_seats[position].is_enabled():
            print('This seat is already taken!')
            return False
        
        elif airplane_seats[position].get_attribute('text') == 'EXIT':
            self.check_warning()
            airplane_seats[position].click()
            print('Seat availabe: exit row')
            return True
        
        elif airplane_seats[position].find_elements_by_tag_name('path')[1].get_attribute('fill') == self.__BLUE_SEATS:
            print('This seat is a preffered seat!')
            return False
        
        elif airplane_seats[position].find_elements_by_tag_name('path')[1].get_attribute('fill') == self.__GREEN_SEATS:
            airplane_seats[position].click()
            print('Seat availabe: standart seat')
            return True

    def check_seat_num(self, seat):
        lines = ['A','B','C','D','E','F','G','H','J','K']
        seat_num = lines.index(seat.capitalize())
        return seat_num

    def click_selection_seat(self):
        self.click(self.__SEAT_BUTTON)

    def click_confirm(self):
        self.click(self.__CONFIRM_BUTTON)
    
    def click_exit_seat(self):
        self.click(self.__EXIT_SEAT_BUTTON)
    
    def check_warning(self):
        if self.driver.find_element(*self.__EXIT_SEAT_BUTTON):
            self.click(self.__EXIT_SEAT_BUTTON)

    def screenshot(self):
        self.driver.find_element(*self.__SEAT_SELECTION_BOX).screenshot('seat_selection.png')
