from selenium.webdriver.support.select import Select
from Model.address import address


class AddressHelper:

    def __init__(self, app):
        self.app = app

    def add_address(self, address):
        wd = self.app.wd
        self.open_home_page()
        self.open_add_address()
        self.fill_address_form(address)
        self.submit_add_address()
        self.return_home_page()
        self.contact_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.get("http://localhost:8080/addressbook/")

    def fill_address_form(self, address):
        wd = self.app.wd
        self.type_address_value("firstname", address.firstname)
        self.type_address_value("lastname", address.lastname)
        self.type_address_value("nickname", address.nickname)
        self.type_address_value("address", address.location)
        self.type_address_value("email", address.email)
        self.type_address_value("mobile", address.phone)

    def type_address_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("Send e-Mail")) > 0):
            wd.find_element_by_link_text("home").click()

    def submit_add_address(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()


    def del_address_by_index(self, index):
        wd = self.app.wd
        #select first address
        self.select_some_address(index)
        #select delete button
        wd.find_element_by_xpath("//div[@class='left'][2]/input").click()
        #click ok on allert
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def select_first_address(self):
        wd = self.app.wd
        self.select_some_address(0)
        self.select_editsome_address(0)

    def select_some_address(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_editsome_address(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def edit_some_address(self, index, new_address_data):
        wd = self.app.wd
        self.return_home_page()
        self.select_editsome_address(index)
        #click on edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        #Change text
        self.fill_address_form(new_address_data)
        #Update
        wd.find_element_by_name("update").click()
        self.contact_cache = None


    def open_add_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def count_address(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    contact_cache = None

    def get_address_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                cells = element.find_elements_by_tag_name("td")
                l_name = cells[1].text
                f_name = cells[2].text
                self.contact_cache.append(address(firstname=f_name, lastname=l_name, id=id))
        return list(self.contact_cache)
