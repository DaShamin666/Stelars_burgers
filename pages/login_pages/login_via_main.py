from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginViaMainPage(BasePage):
    """Вход через главную страницу."""

    _login_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_large__G21Vg') and text()='Войти в аккаунт']")
    _email = (By.XPATH, "//input[contains(@class, 'text') and contains(@class, 'input__textfield') and contains(@class, 'text_type_main-default') and @name='name']")
    _password = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='Пароль' and @type='password']")
    _sign_in_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open(self):
        """Открыть главную страницу."""
        self.driver.get(self._base_url)
        self.url_contains(self._base_url)

    def sign_in_from_main(self, email, password):
        """Выполнить вход через главную страницу."""
        self.click(self._login_btn)
        self.fill(self._email, email)
        self.fill(self._password, password)
        self.click(self._sign_in_btn)
        self.url_contains(self._base_url)
