from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProfileExitPage(BasePage):
    """Выход из профиля."""

    _login_path = "login"
    _email = (By.XPATH, "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _password = (By.XPATH, "//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _sign_in_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")
    _profile_btn = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]")
    _exit_btn = (By.XPATH, "//button[contains(@class, 'Account_button__14Yp3') and contains(@class, 'text') and contains(@class, 'text_type_main-medium') and contains(@class, 'text_color_inactive') and text()='Выход']")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open_login(self):
        """Открыть страницу логина."""
        self.driver.get(f"{self._base_url}{self._login_path}")
        self.url_contains(self._login_path)

    def sign_in(self, email, password):
        """Выполнить вход в систему."""
        self.fill(self._email, email)
        self.fill(self._password, password)
        self.click(self._sign_in_btn)

    def go_to_profile(self):
        """Перейти в личный кабинет."""
        self.click(self._profile_btn)

    def logout(self):
        """Выйти из системы."""
        self.click(self._exit_btn)

    def check_logout(self):
        """Проверить, что выполнен выход (переход на логин)."""
        self.url_contains(self._login_path)
