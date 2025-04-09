import os
import time
from datetime import datetime

def capture_screenshot(driver, test_name):
    """Capture screenshot on test failure"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_dir = "screenshots"
    
    if not os.path.exists(screenshot_dir):
        os.makedirs(screenshot_dir)
    
    file_path = f"{screenshot_dir}/{test_name}_{timestamp}.png"
    driver.save_screenshot(file_path)
    return file_path

def generate_random_name():
    """Generate random employee name for testing"""
    import random
    first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah"]
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller"]
    return (
        f"{random.choice(first_names)}_{random.randint(1,1000)}",
        random.choice(last_names)
    )

def wait_for_element(driver, locator, timeout=10):
    """Custom wait for element with explicit wait"""
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def make_api_request(method, url, headers=None, payload=None):
    """Helper for making API requests"""
    import requests
    response = requests.request(
        method=method,
        url=url,
        headers=headers or {},
        json=payload or {}
    )
    return response
