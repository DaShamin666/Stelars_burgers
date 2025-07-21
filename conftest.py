import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.environments import get_env_config, get_user
from pages.registration_page import RegistrationPage
from pages.sign_in_profile_button import SignIn
from pages.sign_in_button_in_registration import SignInRegistrationPage
from pages.sign_in_password_recovery import SignInPasswordRecoveryPage
from pages.sign_in_to_your_account import LogInToYourAccountPage
from pages.passage import Passage
from pages.exit_in_profile import ExitInProfile
from pages.buns_sauces_fillings_passages import BunsSauceFillingsPassagesPage
from data.credentials import Credentials

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

@pytest.fixture(scope="function")
def driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    device = request.config.getoption("--device")
    width, height = DEVICE_PRESETS.get(device, (1280, 800))
    driver = create_driver(browser, headless, width, height)
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def env_config(request):
    env_name = request.config.getoption("--env")
    return get_env_config(env_name)

@pytest.fixture(scope="function")
def user(request, env_config):
    user_type = request.config.getoption("--user-type") or env_config.default_user
    return get_user(user_type)

@pytest.fixture(scope="session")
def links():
    """Фикстура с основными ссылками для тестов."""
    host = "https://stellarburgers.nomoreparties.site/"
    return {
        "HOST": host,
        "USER_PROFILE": f"{host}account/profile",
        "LOGIN": f"{host}login",
        "REGISTER": f"{host}register",
        "FORGOT_PASSWORD": f"{host}forgot-password"
    }

@pytest.fixture
def registration_page(driver, links):
    return RegistrationPage(driver, links)

@pytest.fixture
def sign_in_page(driver, links):
    return SignIn(driver, links)

@pytest.fixture
def sign_in_profile_registration(driver, links):
    return SignInRegistrationPage(driver, links)

@pytest.fixture
def sign_in_password_recovery(driver, links):
    return SignInPasswordRecoveryPage(driver, links)

@pytest.fixture
def log_in_to_your_account(driver, links):
    return LogInToYourAccountPage(driver, links)

@pytest.fixture
def passage(driver, links):
    return Passage(driver, links)

@pytest.fixture
def exit_in_profile(driver, links):
    return ExitInProfile(driver, links)

@pytest.fixture
def buns_passages(driver, links):
    return BunsSauceFillingsPassagesPage(driver, links)

@pytest.fixture
def dev_user():
    env = get_env_config("DEV")
    return get_user(env.default_user)

@pytest.fixture
def random_user():
    """Генерирует случайного пользователя для теста регистрации."""
    return Credentials().generate_user()


