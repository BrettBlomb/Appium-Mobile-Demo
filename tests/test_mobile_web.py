from appium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mobile_browser():
    options = Options()
    options.add_argument("--disable-notifications")
    
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Android Emulator",
        "browserName": "Chrome",
    }

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options,
        desired_capabilities=desired_caps
    )

    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/")
    title_element = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))
    
    assert "The Internet" in driver.title

    driver.quit()
