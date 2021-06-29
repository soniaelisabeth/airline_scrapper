from selenium.webdriver.common.by import By
from lib import Lib
import logging

class SeatsPage(Lib):

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
        row = '19'
        seat = 'd'
        position_seat = self.check_seat_num(seat)

        airplane_rows = self.driver.find_element_by_class_name(f'row-{row}')
        airplane_seats = airplane_rows.find_elements_by_class_name('gordian-seat')

        if not airplane_seats[position_seat].is_enabled():
            print('this seat is already taken!')
            return False
        
        if airplane_seats[position_seat].get_attribute('text') == 'EXIT':
            print('seat availabe, its on exit row')
            return True
        
        elif airplane_seats[position_seat] in self.new_list:
            print('seat availabe, standart seat')
            return True

        print('')

    def check_seat_num(self, seat):
        lines = ['A','B','C','D','E','F','G','H','J','K'] ##replace with find elements of letters row
        seat_num = lines.index(seat.capitalize())
        return seat_num
    
    def get_green_seats(self):
        green_seats = self.driver.find_elements_by_xpath("//*[@fill='#AADB72']")
        self.new_list = []
        for green_seat in green_seats:
            a = green_seat.find_element_by_xpath("./../..")
            self.new_list.append(a)
        return self.new_list

    def select_seat(self):
        selection_button = self.driver.find_elements_by_id("select-seat")
        selection_button.click()
    
    def screenshot(self):
        ...
