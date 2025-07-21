from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginViaPasswordRecoveryPage(BasePage):
    """Вход через форму восстановления пароля."""

    _path = "login"
    _recovery_link = (By.XPATH, "//a[contains(@class, 'Auth_link__1fOlj') and text()='Восстановить пароль']")
    _email = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _recovery_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Восстановить']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open(self):
        """Открыть страницу логина."""
        self.driver.get(f"{self._base_url}{self._path}")
        self.url_contains(self._path)

    def sign_in_from_recovery(self, email, password):
        """Выполнить вход через восстановление пароля."""
        self.click(self._recovery_link)
        self.fill(self._email, email)
        self.click(self._recovery_btn)
        # Здесь добавить шаги для входа, если появится форма логина после восстановления
