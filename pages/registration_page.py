from pages.base_page import BasePage



class RegistrationPage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["REGISTER"]

    # Локаторы элементов

    _NAME_FIELD = ("xpath","//input[contains(@class, 'input__textfield') and @name='name' and @type='text']")
    _EMAIL_FIELD = ("xpath", "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _PASSWORD_FIELD = ("xpath","//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _BUTTON_FIELD = ("xpath","//button[contains(@class, 'button_button') and text()='Зарегистрироваться']")
    _INPUT_EMAIL_SIGN_IN = ("xpath","//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _INPUT_PASSWORD_SIGN_IN = ("xpath",
                               "//input[@class='text input__textfield text_type_main-default' and @type='password'"
                               " and @name='Пароль']")
    _BUTTON_FIELD_IN_SIGN_IN = ("xpath","//button[contains(@class, 'button_button__33qZ0')"
                                " and contains(@class,"
                                " 'button_button_type_primary__1O7Bx')"
                                " and contains(@class, 'button_button_size_medium__3zxIa')]")


    def input_name(self, name):
        """Вводит имя пользователя в поле регистрации."""
        self.input_text(self._NAME_FIELD, name)

    def input_email(self, email):
        """Вводит email пользователя в поле регистрации."""
        self.input_text(self._EMAIL_FIELD, email)

    def input_password(self, password):
        """Вводит пароль пользователя в поле регистрации."""
        self.input_text(self._PASSWORD_FIELD, password)

    def click_button(self):
        """Кликает по кнопке регистрации."""
        self.click_element(self._BUTTON_FIELD)

    def input_email_on_login(self, email):
        """Вводит email на странице входа."""
        self.input_text(self._INPUT_EMAIL_SIGN_IN, email)

    def input_password_on_login(self, password):
        """Вводит пароль на странице входа."""
        self.input_text(self._INPUT_PASSWORD_SIGN_IN, password)

    def click_button_on_sign_in(self):
        """Кликает по кнопке входа на странице входа."""
        self.click_element(self._BUTTON_FIELD_IN_SIGN_IN)

    def is_registration_successful(self):
        """Проверяет, что после регистрации пользователь оказался на главной странице."""
        assert self.driver.current_url == self._links["HOST"], f"Регистрация неуспешна: {self.driver.current_url} != {self._links['HOST']}"
        return True

    def is_registration_not_sucsess(self):
        """Проверяет, что после неуспешной регистрации пользователь остался на странице регистрации."""
        assert self.driver.current_url == self._links["REGISTER"], f"Ожидалось остаться на странице регистрации, но URL: {self.driver.current_url}"
        return True

    def open(self):
        """Открывает страницу регистрации."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу регистрации: {self.driver.current_url}"