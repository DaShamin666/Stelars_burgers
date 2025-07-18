import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import allure


DEVICE_PRESETS = {
    "mobile": (375, 667),
    "tablet": (768, 1024),
    "laptop": (1024, 768),
    "desktop": (1280, 800)
}

def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="chrome/firefox")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--device", default=None, help="mobile/tablet/laptop/desktop")
    parser.addoption("--env", default="dev", help="dev/stage")
    parser.addoption("--user-type", default=None)

def create_driver(browser: str, headless: bool, width: int, height: int):
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")
        return webdriver.Chrome(options=options)
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Browser {browser} not supported")

@pytest.fixture(autouse=True)
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    device = request.config.getoption("--device")
    width, height = DEVICE_PRESETS.get(device, (1280, 800))
    driver = create_driver(browser, headless, width, height)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)


