## 📱 Mobile Web Automation (Appium + Android Emulator)

This project includes automated mobile browser testing using **Appium v3**, **Python**, and **Android Emulator**.

---

## 🔧 Requirements

- Node.js 18+
- Python 3.11+
- Android SDK (API 33 recommended)
- Appium v3
- UiAutomator2 driver
- Chromedriver (matching Chrome version in emulator)

---

## 📦 Installation

### Install Appium

```bash
npm install -g appium@latest
Install Drivers
bash
Copy code
appium driver install uiautomator2
appium driver install chromedriver
⚠ Important: Appium v3 no longer auto-downloads Chromedrivers using capabilities.
You must install the Chromedriver plugin (above) or manually supply Chromedriver 109.

💡 Chrome 109 Driver (Emulator Default)
Most Android emulators still ship with Chrome 109, so you must use Chromedriver 109.

Download Chromedriver 109:

https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_win32.zip

Place chromedriver.exe here:

swift
Copy code
~/.appium/node_modules/appium-uiautomator2-driver/node_modules/appium-chromedriver/chromedriver/win/
▶️ Running Mobile Tests
Start Appium:

bash
Copy code
appium
Run mobile tests:

bash
Copy code
pytest -k mobile
✔ Example Mobile Test
python
Copy code
from appium import webdriver
from appium.options.android import UiAutomator2Options

def test_mobile_browser():
    options = UiAutomator2Options()
    options.set_capability("platformName", "Android")
    options.set_capability("appium:automationName", "UiAutomator2")
    options.set_capability("appium:deviceName", "Android Emulator")
    options.set_capability("appium:browserName", "Chrome")

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.get("https://the-internet.herokuapp.com")

    assert "The Internet" in driver.title
    driver.quit()
