# -*- coding: utf-8 -*-
from selenium import webdriver
from group import group
import unittest

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    
    def test_add_group(self):
        wd = self.wd
        self.Login(wd, "admin", "secret")
        self.create_group(wd, group("name", "footer", "header"))
        self.Logout(wd)

    def test_add_empty_group(self):
            wd = self.wd
            self.Login(wd, "admin", "secret")
            self.create_group(wd, group(" ", " ", " "))
            self.Logout(wd)

    def Logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, group):
        self.open_group_page(wd)
        # init group creation
        wd.find_element_by_name("new").click()
        # fill groups film
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page(wd)

    def open_group_page(self, wd):
        wd.find_element_by_link_text("groups").click()

    def Login(self, wd, username, password):
        self.open_home_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost:8080/addressbook/")


    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
