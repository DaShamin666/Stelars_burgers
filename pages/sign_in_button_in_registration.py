from pages.base_page import BasePage

class SignInRegistrationPage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["REGISTER"]

    _BUTTON_SIGN_IN = ("xpath","//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    _INPUT_EMAIL = ("xpath","//input[contains(@class, 'text input__textfield text_type_main-default') and @name='name']")
    _INPUT_PASSWIRD = ("xpath","//input[contains(@class, 'text input__textfield text_type_main-default') and @type='password' and @name='Пароль']")
    _CLICK_BUTTON_SIGN_IN = ('xpath',"//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']")

    def click_button_profile_registration(self):
        """Кликает по ссылке 'Войти' в форме регистрации."""
        self.click_element(self._BUTTON_SIGN_IN)

    def input_email_on_profile_registration(self, email):
        """Вводит email в форме регистрации."""
        self.input_text(self._INPUT_EMAIL, email)

    def input_password_on_profile_registration(self, password):
        """Вводит пароль в форме регистрации."""
        self.input_text(self._INPUT_PASSWIRD, password)

    def click_button_on_profile_registration_two(self):
        """Кликает по кнопке 'Войти' после ввода данных в форме регистрации и проверяет переход на главную страницу."""
        self.click_element(self._CLICK_BUTTON_SIGN_IN)
        assert self.driver.current_url == self._links["HOST"], f"Ожидался переход на главную после входа, но URL: {self.driver.current_url}"

    def open(self):
        """Открывает страницу регистрации."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу регистрации: {self.driver.current_url}"