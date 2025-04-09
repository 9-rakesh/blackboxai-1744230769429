import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from dotenv import load_dotenv
import os

load_dotenv()

@pytest.fixture(scope="class")
def setup(request):
    browser = os.getenv("BROWSER")
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    
    driver.maximize_window()
    driver.get(os.getenv("BASE_URL"))
    request.cls.driver = driver
    yield
    driver.quit()

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        driver = request.cls.driver
        driver.save_screenshot(f"screenshots/{item.name}.png")
