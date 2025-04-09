# OrangeHRM Test Automation Framework

## Framework Overview
- **Language**: Python 3.x
- **Test Runner**: pytest
- **Pattern**: Page Object Model (POM)
- **Reporting**: HTML reports
- **Browser Support**: Chrome/Firefox

## Prerequisites
- Python 3.7+
- pip package manager
- Chrome/Firefox browser

## Setup Instructions
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env` file:
```ini
BASE_URL=https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
USERNAME=Admin
PASSWORD=admin123
BROWSER=chrome
```

## Running Tests
Execute all tests:
```bash
pytest tests/ --html=report.html
```

Run specific test file:
```bash
pytest tests/test_login.py --html=report.html
```

## Framework Structure
```
.
├── pages/                  # Page object classes
│   ├── base_page.py        # Base page class
│   ├── login_page.py       # Login page
│   ├── dashboard_page.py   # Dashboard page
│   ├── pim_page.py         # PIM module
│   └── employee_list_page.py # Employee list
├── tests/                  # Test scripts
│   ├── test_login.py       # Login tests
│   └── test_pim_workflow.py # PIM workflow tests
├── conftest.py             # Test configuration
├── requirements.txt        # Dependencies
└── .env                    # Environment config
```

## Test Data Management
- Test data is currently hardcoded in test scripts
- For production use, consider externalizing to JSON/Excel files

## Reporting
- HTML reports are generated in the root directory
- Screenshots are captured on test failures (saved in `/screenshots`)
