from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        """Найти элемент с явным ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Нажать на элемент с явным ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def check_url(self, url):
        """Проверка URL после авторизации"""
        assert self.driver.current_url == url, f"URL не соответствует ожидаемому: {url}"

    def attach_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к отчету Allure."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )