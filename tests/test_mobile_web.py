from appium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def test_mobile_browser():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "browserName": "Chrome",
        "deviceName": "Android Emulator",
    }

    driver = webdriver.Remote("http://127.0.0.1:4723", desired_caps)

    driver.get("https://the-internet.herokuapp.com/")
    title = driver.title

    assert "The Internet" in title

    driver.quit()
