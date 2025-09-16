import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from config.environments import get_env_config, get_user
from pages.registration import RegistrationPage
from pages.login_pages.login_via_profile import LoginViaProfilePage
from pages.login_pages.login_via_registration import LoginViaRegistrationPage
from pages.login_pages.login_via_password_recovery import LoginViaPasswordRecoveryPage
from pages.login_pages.login_via_main import LoginViaMainPage
from pages.navigation import NavigationPage
from pages.profile_exit import ProfileExitPage
from pages.ingredients import IngredientsPage
from data.credentials import Credentials

DEVICE_PRESETS = {
    "mobile": (375, 667),
    "tablet": (768, 1024),
    "laptop": (1024, 768),
    "desktop": (1280, 800),
}


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="chrome/firefox")
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )
    parser.addoption("--device", default=None, help="mobile/tablet/laptop/desktop")
    parser.addoption("--env", default="dev", help="dev/stage")
    parser.addoption("--user-type", default=None, help="Type of user for testing")


def create_driver(browser, headless, width, height):
    if browser == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.add_argument(f"--window-size={width},{height}")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-extensions")
        options.add_argument("--remote-debugging-port=9222")
        
        # Для Docker/Linux используем Chromium напрямую
        import os
        import platform
        
        # Проверяем архитектуру и систему
        if platform.system() == "Linux" and platform.machine() == "aarch64":
            # На ARM64 Linux используем Chromium
            options.binary_location = "/usr/bin/chromium"
        elif os.path.exists("/usr/bin/chromium"):
            # Если Chromium доступен, используем его
            options.binary_location = "/usr/bin/chromium"
        
        # Создаем Service для ChromeDriver
        from selenium.webdriver.chrome.service import Service
        
        try:
            # Определяем пути к возможным драйверам
            driver_paths = [
                "/usr/bin/chromedriver",
                "/usr/bin/chromium-driver", 
                "/usr/local/bin/chromedriver"
            ]
            
            # Ищем доступный драйвер
            driver_path = None
            for path in driver_paths:
                if os.path.exists(path) and os.access(path, os.X_OK):
                    driver_path = path
                    break
            
            if driver_path:
                # Если драйвер найден, используем его
                service = Service(driver_path)
                return webdriver.Chrome(service=service, options=options)
            else:
                # Fallback - пытаемся без явного указания пути
                return webdriver.Chrome(options=options)
                
        except Exception as e:
            # Пытаемся использовать webdriver-manager как последнюю попытку
            try:
                from webdriver_manager.chrome import ChromeDriverManager
                service = Service(ChromeDriverManager().install())
                return webdriver.Chrome(service=service, options=options)
            except Exception as inner_e:
                raise Exception(f"Не удалось создать Chrome/Chromium driver. Основная ошибка: {e}, webdriver-manager ошибка: {inner_e}")
    elif browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        
        # Добавляем настройки для Docker-контейнера
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        
        # Создаем Service для GeckoDriver
        from selenium.webdriver.firefox.service import Service
        import os
        
        try:
            # Определяем пути к возможным драйверам
            driver_paths = [
                "/usr/local/bin/geckodriver",
                "/usr/bin/geckodriver"
            ]
            
            # Ищем доступный драйвер
            driver_path = None
            for path in driver_paths:
                if os.path.exists(path) and os.access(path, os.X_OK):
                    driver_path = path
                    break
            
            if driver_path:
                # Если драйвер найден, используем его
                service = Service(driver_path)
                driver = webdriver.Firefox(service=service, options=options)
            else:
                # Fallback - пытаемся без явного указания пути
                driver = webdriver.Firefox(options=options)
                
            driver.set_window_size(width, height)
            return driver
            
        except Exception as e:
            raise Exception(f"Не удалось создать Firefox driver: {e}")
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


@pytest.fixture
def registration_page(driver, env_config):
    return RegistrationPage(driver, env_config.url)


@pytest.fixture
def login_profile_page(driver, env_config):
    return LoginViaProfilePage(driver, env_config.url)


@pytest.fixture
def login_registration_page(driver, env_config):
    return LoginViaRegistrationPage(driver, env_config.url)


@pytest.fixture
def login_recovery_page(driver, env_config):
    return LoginViaPasswordRecoveryPage(driver, env_config.url)


@pytest.fixture
def login_main_page(driver, env_config):
    return LoginViaMainPage(driver, env_config.url)


@pytest.fixture
def navigation_page(driver, env_config):
    return NavigationPage(driver, env_config.url)


@pytest.fixture
def profile_exit_page(driver, env_config):
    return ProfileExitPage(driver, env_config.url)


@pytest.fixture
def ingredients_page(driver, env_config):
    return IngredientsPage(driver, env_config.url)


@pytest.fixture
def random_user():
    return Credentials().generate_user()
