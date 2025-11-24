from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_mobile_browser():
    # Appium v2 capability style (prefix appium:)
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:deviceName", "Android Emulator")
    options.set_capability("appium:browserName", "Chrome")

    # ⭐ Correct capability name
    options.set_capability("appium:chromedriver_autodownload", True)

    # Stability: ensure webview loads
    options.set_capability("appium:ensureWebviewsHavePages", True)
    options.set_capability("appium:nativeWebScreenshot", True)

    # Connect to Appium
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # Wait for webview
    driver.execute_script("mobile: waitForWebview", {"timeout": 15000})

    wait = WebDriverWait(driver, 20)

    # Navigate
    driver.get("https://the-internet.herokuapp.com/")
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

    assert "The Internet" in driver.title

    driver.quit()
