from selenium.webdriver.firefox.webdriver import WebDriver
from Fixture.session import SessionHelper
from Fixture.group import GroupHelper
from Fixture.contacts import AddressHelper


class Application:


    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.Contacts = AddressHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False



    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/addressbook/")


    def destroy(self):
        self.wd.quit()