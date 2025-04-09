import pytest
import json
import os
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage
from pages.employee_list_page import EmployeeListPage

def load_test_data(file_name):
    with open(os.path.join('test_data', file_name)) as f:
        return json.load(f)

@pytest.mark.usefixtures("setup")
class TestPIMWorkflow:
    @pytest.mark.parametrize("employee", load_test_data('employee_data.json')['valid_employees'])
    def test_add_and_verify_employees(self, setup, employee):
        # Login
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        # Navigate to PIM
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_pim()

        # Add employee
        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_add_employee()
        pim_page.add_employee(employee['first_name'], employee['last_name'])
        assert "Successfully Saved" in pim_page.get_success_message()

        # Verify employee in list
        pim_page.navigate_to_employee_list()
        employee_list_page = EmployeeListPage(self.driver)
        full_name = f"{employee['first_name']} {employee['last_name']}"
        employee_list_page.search_employee(full_name)
        assert employee_list_page.verify_employee_in_list(full_name)
        print(f"Name Verified: {full_name}")

        # Logout
        dashboard_page.logout()
        assert "auth/login" in self.driver.current_url

    @pytest.mark.parametrize("employee", load_test_data('employee_data.json')['invalid_employees'])
    def test_add_invalid_employees(self, setup, employee):
        # Login
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        # Navigate to PIM
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.navigate_to_pim()

        # Attempt to add invalid employee
        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_add_employee()
        pim_page.add_employee(employee['first_name'], employee['last_name'])
        
        # Verify error message
        if not employee['first_name']:
            assert "Required" in pim_page.get_error_message()
        if not employee['last_name']:
            assert "Required" in pim_page.get_error_message()
