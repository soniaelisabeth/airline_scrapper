from lib import Lib
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
    seat = str(input('Seat Letter: '))

    seats_page.get_green_seats()
    position = seats_page.check_seat_num(seat)
    if not seats_page.locate_seats(row,position):
        print('Sorry! Try again!')
    
    seats_page.click_selection_seat()
    seats_page.click_confirm()
