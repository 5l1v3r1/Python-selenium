from selenium.webdriver.support.select import Select


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_address(self, address):
        wd = self.app.wd
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


    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def submit_add_address(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def add_birthday(self):
        wd = self.app.wd
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


    def add_work(self):
        wd = self.app.wd
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("qa")

    def del_first_address(self):
        wd = self.app.wd
        #select first address
        wd.find_element_by_name("selected[]").click()
        #select delete button
        wd.find_element_by_xpath("//div[@class='left'][2]/input").click()
        #click ok on allert
        wd.switch_to_alert().accept()


    def edit_address(self, address):
        wd = self.app.wd
        #click on edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #Change text
        self.add_address(address)
        #Update
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def open_edit_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()


    def add_image(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()