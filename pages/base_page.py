from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find(self, locator):
        """Явно дождаться и найти элемент по локатору."""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """Явно дождаться и кликнуть по элементу."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def fill(self, locator, value):
        """Очистить и ввести значение в поле."""
        element = self.find(locator)
        element.clear()
        element.send_keys(value)

    def is_visible(self, locator):
        """Проверить видимость элемента."""
        try:
            return self.find(locator).is_displayed()
        except Exception:
            return False

    def url_contains(self, part):
        """Проверить, что текущий url содержит подстроку."""
        assert part in self.driver.current_url, (
            f"URL не содержит '{part}': {self.driver.current_url}"
        )

    def attach_screenshot(self, name="screenshot"):
        """Прикрепить скриншот к Allure-отчету."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG,
        )
