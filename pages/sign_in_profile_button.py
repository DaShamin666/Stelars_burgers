from pages.base_page import BasePage

class SignIn(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["HOST"]

    _BUTTON_PROFILE = ('xpath',"//p[contains(@class,"
                               " 'AppHeader_header__linkText__3q_va') and contains(@class,"
                               " 'ml-2') and text()='Личный Кабинет']")
    _INPUT_EMAIL_SIGN_IN = ("xpath", "//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _INPUT_PASSWORD_SIGN_IN = ("xpath",
                               "//input[@class='text input__textfield text_type_main-default' and @type='password'"
                               " and @name='Пароль']")
    _BUTTON_FIELD_SIGN_IN = ("xpath", "//button[contains(@class, 'button_button__33qZ0')"
                                         " and contains(@class,"
                                         " 'button_button_type_primary__1O7Bx')"
                                         " and contains(@class, 'button_button_size_medium__3zxIa')]")

    def click_button_on_sign_in_profile(self):
        """Кликает по кнопке 'Личный кабинет' в хедере."""
        self.click_element(self._BUTTON_PROFILE)

    def input_email_on_sign_in(self, email):
        """Вводит email на странице входа."""
        self.input_text(self._INPUT_EMAIL_SIGN_IN, email)

    def input_password_on_sign_in(self, password):
        """Вводит пароль на странице входа."""
        self.input_text(self._INPUT_PASSWORD_SIGN_IN, password)

    def click_button_on_sign(self):
        """Кликает по кнопке входа на странице входа и проверяет успешный вход."""
        self.click_element(self._BUTTON_FIELD_SIGN_IN)
        assert self.driver.current_url == self._links["HOST"], f"Ожидался переход на главную после входа, но URL: {self.driver.current_url}"

    def open(self):
        """Открывает страницу авторизации."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу авторизации: {self.driver.current_url}"


