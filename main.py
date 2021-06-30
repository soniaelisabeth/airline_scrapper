from lib import Lib
from time import sleep
from seats_page import SeatsPage

lib = Lib()
driver = lib.start_browser()
seats_page = SeatsPage(driver)
website = 'https:\\static.gordiansoftware.com'
seats_page.open_page(website)

print('Welcome to the flight selector!')
flights = [1,2]

for flight in flights:
    print('Choose your seats!')
    row = int(input('Seat Number: '))

    if row > 60 or row < 18:
        print('Please, select a valid seat number!')
        break

    seat = str(input('Seat Letter: '))
    if seat.isnumeric():
        print('Please, select a letter!')
        break

    position = seats_page.check_seat_num(seat)
    
    if not seats_page.locate_seats(row,position):
        print('Sorry! Try again!')
        break
    
    seats_page.click_selection_seat()
    seats_page.click_confirm()


seats_page.screenshot()
