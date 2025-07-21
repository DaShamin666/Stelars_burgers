from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginViaProfilePage(BasePage):
    """Вход через кнопку 'Личный кабинет'."""

    _profile_btn = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText__3q_va') and contains(@class, 'ml-2') and text()='Личный Кабинет']")
    _email = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _password = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']")
    _sign_in_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open(self):
        """Открыть главную страницу."""
        self.driver.get(self._base_url)
        self.url_contains(self._base_url)

    def open_login(self):
        """Перейти на страницу логина через 'Личный кабинет'."""
        self.click(self._profile_btn)
        self.url_contains("login")

    def sign_in(self, email, password):
        """Выполнить вход по email и паролю."""
        self.fill(self._email, email)
        self.fill(self._password, password)
        self.click(self._sign_in_btn)
        self.url_contains(self._base_url)

    def sign_in_via_profile(self, email, password):
        """Полный процесс входа через 'Личный кабинет'."""
        self.open_login()
        self.sign_in(email, password)
