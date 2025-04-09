import pytest
from utils.helpers import make_api_request

@pytest.mark.api
class TestOrangeHRMAPI:
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2"
    
    def test_get_employee_list(self):
        """Test getting employee list through API"""
        response = make_api_request(
            method="GET",
            url=f"{self.BASE_URL}/pim/employees",
            headers={"Authorization": "Bearer valid_token_here"} 
        )
        assert response.status_code == 200
        assert isinstance(response.json()["data"], list)

    def test_create_employee(self):
        """Test creating employee through API"""
        test_employee = {
            "firstName": "API",
            "lastName": "Test",
            "employeeId": "1001"
        }
        response = make_api_request(
            method="POST",
            url=f"{self.BASE_URL}/pim/employees",
            headers={"Authorization": "Bearer valid_token_here"},
            payload=test_employee
        )
        assert response.status_code == 201
        assert response.json()["data"]["firstName"] == "API"
