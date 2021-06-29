from selenium.webdriver.common.by import By
from lib import Lib
import logging

class SeatsPage(Lib):
    __SEAT_BUTTON = (By.ID, 'select-seat')
    __CONFIRM_BUTTON = (By.ID, 'next-button')
    __GREEN_SEATS = (By.XPATH, "//*[@fill='#AADB72']")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    def locate_seats(self, row, position):
        airplane_rows = self.driver.find_element_by_class_name(f'row-{row}')
        airplane_seats = airplane_rows.find_elements_by_class_name('gordian-seat')

        if not airplane_seats[position].is_enabled():
            print('this seat is already taken!')
            return False
        
        if airplane_seats[position].get_attribute('text') == 'EXIT':
            airplane_seats[position].click()
            print('seat availabe, its on exit row')
            return True
        
        elif airplane_seats[position] in self.seats_list:
            airplane_seats[position].click()
            print('seat availabe, standart seat')
            return True

        print('')

    def check_seat_num(self, seat):
        lines = ['A','B','C','D','E','F','G','H','J','K'] ##replace with find elements of letters row
        seat_num = lines.index(seat.capitalize())
        return seat_num
    
    def get_green_seats(self):
        green_seats = self.driver.find_elements_by_xpath(self.__GREEN_SEATS)
        self.seats_list = []
        for green_seat in green_seats:
            seat = green_seat.find_element_by_xpath("./../..")
            self.seats_list.append(seat)
        return self.seats_list

    def click_selection_seat(self):
        self.click(self.__SEAT_BUTTON)

    def click_confirm(self):
        self.click(self.__CONFIRM_BUTTON)

    def screenshot(self):
        ...
