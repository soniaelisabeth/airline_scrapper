from lib import Lib
from seats_page import SeatsPage

lib = Lib()
driver = lib.start_browser()
seats_page = SeatsPage(driver)

if not seats_page.open_page('https:\\static.gordiansoftware.com'):
    print('Sorry! Try again!')