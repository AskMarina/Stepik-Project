
from pages.main_page import MainPage

from selenium.webdriver.common.by import By
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # initialize the Page Object, pass the driver instance and the url to the constructor
    page = MainPage(browser, link)
    page.open() # opening the page
    # executing the page method — go to the login page
    page.go_to_login_page()