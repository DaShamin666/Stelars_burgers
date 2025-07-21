from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NavigationPage(BasePage):
    """Навигация по логотипу."""

    _login_path = "login"
    _logo = (By.XPATH, '//*[@id="root"]/div/header/nav/div')

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open_login(self):
        """Открыть страницу логина."""
        self.driver.get(f"{self._base_url}{self._login_path}")
        self.url_contains(self._login_path)

    def click_logo(self):
        """Кликнуть по логотипу Stellar Burgers."""
        self.click(self._logo)

    def check_main_opened(self):
        """Проверить, что открыта главная страница."""
        self.url_contains(self._base_url)
