from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    """Страница регистрации пользователя."""

    _path = "register"
    _name = (By.XPATH, "//input[contains(@class, 'input__textfield') and @name='name' and @type='text']")
    _email = (By.XPATH, "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _password = (By.XPATH, "//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _register_btn = (By.XPATH, "//button[contains(@class, 'button_button') and text()='Зарегистрироваться']")
    _login_email = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _login_password = (By.XPATH, "//input[@class='text input__textfield text_type_main-default' and @type='password' and @name='Пароль']")
    _login_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self._base_url = base_url

    def open(self):
        """Открыть страницу регистрации."""
        self.driver.get(f"{self._base_url}{self._path}")
        self.url_contains(self._path)

    def fill_form(self, name, email, password):
        """Заполнить форму регистрации."""
        self.fill(self._name, name)
        self.fill(self._email, email)
        self.fill(self._password, password)

    def submit(self):
        """Отправить форму регистрации."""
        self.click(self._register_btn)

    def login_after_registration(self, email, password):
        """Войти после успешной регистрации."""
        self.fill(self._login_email, email)
        self.fill(self._login_password, password)
        self.click(self._login_btn)

    def check_failed(self):
        """Проверить, что регистрация не удалась (остались на странице регистрации)."""
        self.url_contains(self._path)
