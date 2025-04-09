from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class EmployeeListPage(BasePage):
    EMPLOYEE_NAME_SEARCH = (By.XPATH, "//label[text()='Employee Name']/following::input[1]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".oxd-table-card")

    def __init__(self, driver):
        super().__init__(driver)

    def search_employee(self, name):
        self.enter_text(self.EMPLOYEE_NAME_SEARCH, name)
        self.click(self.SEARCH_BUTTON)

    def verify_employee_in_list(self, name):
        results = self.driver.find_elements(*self.SEARCH_RESULT)
        for result in results:
            if name in result.text:
                return True
        return False
