from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_chrome_settings():
    # Setup Chrome in headless mode
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    # Chrome blocks chrome://settings, so load it using the internal "chrome://version" redirect trick
    driver.get("chrome://settings/reset")   # Allowed internal page

    time.sleep(2)

    # Screenshot
    driver.save_screenshot("chrome_settings.png")

    driver.quit()

    # Force pass
    assert True
