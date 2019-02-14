# -*- coding: utf-8 -*-
from selenium import webdriver
from address import address
from selenium.webdriver.support.ui import Select
import unittest

class TestAddAddress(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_address(self): 
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, "admin", "secret")
        self.open_edit_address(wd)
        self.add_address(wd, address('firstname', 'lastname', 'nickname', 'location', 'email', 'phone'))
        self.add_work(wd)
        self.add_birthday(wd)
        self.submit_add_address(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def test_add_empty_address(self):
        wd = self.wd
        self.open_home_page(wd)
        self.Login(wd, "admin", "secret")
        self.open_edit_address(wd)
        self.add_address(wd, address(' ', ' ', ' ', ' ', ' ', ' '))
        self.submit_add_address(wd)
        self.return_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit_add_address(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_birthday(self, wd):
        #Day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("31")
        wd.find_element_by_xpath("//option[@value='31']").click()
        #Month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("July")
        wd.find_element_by_xpath("//option[@value='July']").click()
        #year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1992")


    def add_work(self, wd):
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("qa")



    def add_address(self, wd, address):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(address.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(address.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(address.nickname)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.location)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(address.email)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(address.phone)

    def Login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")

    def open_edit_address(self, wd):
        wd.find_element_by_link_text("add new").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
