from selenium.webdriver.support.select import Select


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_address(self, address):
        wd = self.app.wd
        self.fill_address_form(address)

    def fill_address_form(self, address):
        wd = self.app.wd
        self.type_address_none("firstname", address.firstname)
        self.type_address_none("lastname",address.lastname)
        self.type_address_none("nickname", address.nickname)
        self.type_address_none("address", address.location)
        self.type_address_none("email", address.email)
        self.type_address_none("mobile", address.phone)

    def type_address_none(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

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


    def edit_address(self, new_address_data):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        #click on edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #Change text
        self.fill_address_form(new_address_data)
        #Update
        wd.find_element_by_name("update").click()

    def open_edit_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
