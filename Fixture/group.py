from Model.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("group page").click()


    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill groups film
        self.fill_group_from(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()
        self.group_cache = None

    def fill_group_from(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def delete_first_group(self):
        self.delete_group_by_index(0)



    def edit_first_group(self):
        self.edit_group_by_index(0)


    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        #select first group
        self.select_group_by_index(index)
        #submit deleteion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.group_cache = None


    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        # select first group
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        #change text
        self.fill_group_from(new_group_data)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.group_cache = None

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def countgroup(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    #Добавил КЕШ
    group_cache = None


    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)


