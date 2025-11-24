## 📱 Mobile Web Automation (Appium + Android Emulator)

This project includes mobile browser automation using **Appium v3** and **UiAutomator2**.

### 🔧 Requirements

- Node.js >= 18
- Python 3.11+
- Android SDK (with `platform-tools`, `build-tools`, and at least API 33)
- Appium v3
- Appium UIAutomator2 driver
- Chromedriver (version matching Chrome inside the emulator)

### 📦 Installation

#### Install Appium
```bash
npm install -g appium@latest
Install UiAutomator2 Driver
bash
Copy code
appium driver install uiautomator2
Install Chromedriver Manager Plugin
Appium 3 no longer auto-downloads Chromedrivers by capability.

bash
Copy code
appium driver install chromedriver
▶️ Running Mobile Tests
Start Appium:

bash
Copy code
appium
Run the tests:

bash
Copy code
pytest -k mobile
⚠ ChromeDriver for Chrome 109
The Android emulator ships with Chrome 109, which requires the matching Chromedriver.

Download:
https://chromedriver.storage.googleapis.com/109.0.5414.74/chromedriver_win32.zip

Place into:

swift
Copy code
~/.appium/.../appium-chromedriver/chromedriver/win/
✔ Example Test
python
Copy code
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
