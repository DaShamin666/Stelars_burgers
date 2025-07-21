from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginViaRegistrationPage(BasePage):
    """Вход через ссылку на странице регистрации."""

    _path = "register"
    _sign_in_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    _email = (By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default') and @name='name']")
    _password = (By.XPATH, "//input[contains(@class, 'text input__textfield text_type_main-default') and @type='password' and @name='Пароль']")
    _sign_in_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open(self):
        """Открыть страницу регистрации."""
        self.driver.get(f"{self._base_url}{self._path}")
        self.url_contains(self._path)

    def sign_in_from_registration(self, email, password):
        """Выполнить вход через форму на странице регистрации."""
        self.click(self._sign_in_link)
        self.fill(self._email, email)
        self.fill(self._password, password)
        self.click(self._sign_in_btn)
        self.url_contains(self._base_url)
