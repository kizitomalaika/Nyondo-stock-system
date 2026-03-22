from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest

BASE_URL = "https://kizitomalaika.github.io/Nyondo-stock-system/stock.html"

@pytest.fixture
def driver():
    """Set up chrome for each test"""
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_page_loads(driver):
    """Test the stock registration form loads successfully"""
    driver.get(BASE_URL)
    assert "NyondoStock" in driver.title
    print("Page loaded successfully")

def test_required_fields_exist(driver):
    """Test that all required fields are present on the form"""
    driver.get(BASE_URL)
    assert driver.find_element(By.ID, "product-id")
    assert driver.find_element(By.ID, "product-name")
    assert driver.find_element(By.ID, "category")
    assert driver.find_element(By.ID, "unit")
    assert driver.find_element(By.ID, "description")
    assert driver.find_element(By.ID, "quantity")
    assert driver.find_element(By.ID, "unit-price")
    assert driver.find_element(By.ID, "reorder-level")
    assert driver.find_element(By.ID, "date-received")
    assert driver.find_element(By.ID, "expiry-date")
    assert driver.find_element(By.ID, "supplier")
    assert driver.find_element(By.ID, "batch-number")
    assert driver.find_element(By.ID, "storage-location")
    assert driver.find_element(By.ID, "stock-status")
    print("All required fields found")

def test_sidebar_visible(driver):
    """Test that the sidebar is visible on the paga"""
    driver.get(BASE_URL)
    sidebar = driver.find_element(By.CLASS_NAME, "sidebar")
    assert sidebar.is_displayed()
    print("Side bar is visible")

def test_active_nav_item(driver):
    """Test that stock Management is the active nav item in sidebar"""
    driver.get(BASE_URL)
    nav_items = driver.find_elements(By.CLASS_NAME, "nav-item")
    active_items = [item for item in nav_items if "active" in item.get_attribute("class")]
    assert len(active_items) ==1
    assert "Stock Management" in active_items[0].text
    print("Stock Management is active") 
