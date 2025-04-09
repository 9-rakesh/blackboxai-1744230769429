from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    ADD_EMPLOYEE_BUTTON = (By.LINK_TEXT, "Add Employee")
    EMPLOYEE_LIST_BUTTON = (By.LINK_TEXT, "Employee List")
    FIRST_NAME_FIELD = (By.NAME, "firstName")
    LAST_NAME_FIELD = (By.NAME, "lastName")
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "oxd-toast-content")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".oxd-input-field-error-message")

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_add_employee(self):
        self.click(self.ADD_EMPLOYEE_BUTTON)

    def navigate_to_employee_list(self):
        self.click(self.EMPLOYEE_LIST_BUTTON)

    def add_employee(self, first_name, last_name):
        self.enter_text(self.FIRST_NAME_FIELD, first_name)
        self.enter_text(self.LAST_NAME_FIELD, last_name)
        self.click(self.SAVE_BUTTON)

    def get_success_message(self):
        return self.get_element_text(self.SUCCESS_MESSAGE)
        
    def get_error_message(self):
        return self.get_element_text(self.ERROR_MESSAGE)
