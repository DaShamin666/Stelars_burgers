from pages.base_page import BasePage



class LogInToYourAccountPage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["HOST"]

    _BUTTON_LOG_TO_YOU_ACCOUNT =("xpath","//button[contains(@class, 'button_button__33qZ0')"
                                         " and contains(@class, 'button_button_type_primary__1O7Bx')"
                                         " and contains(@class, 'button_button_size_large__G21Vg')"
                                         " and text()='Войти в аккаунт']")
    _INPUT_EMAIL_LOG_TO_YOU_ACCOUNT = ("xpath","//input[contains(@class, 'text')"
                                               " and contains(@class, 'input__textfield')"
                                               " and contains(@class, 'text_type_main-default') and @name='name']")
    _INPUT_PASSWORD_LOG_TO_YOU_ACCOUNT = ("xpath","//input[@class='text input__textfield text_type_main-default'"
                                                  " and @name='Пароль' and @type='password']")
    _BUTTON_LOG_TO_ACCOUNT = ("xpath","//button[contains(@class, 'button_button__33qZ0')"
                                      " and contains(@class, 'button_button_type_primary__1O7Bx')"
                                      " and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']")

    def click_log_in_to_your_account(self):
        """Кликает по кнопке 'Войти в аккаунт' на главной странице."""
        self.click_element(self._BUTTON_LOG_TO_YOU_ACCOUNT)

    def input_email_log_to_your_account(self, email):
        """Вводит email на форме входа на главной странице."""
        self.input_text(self._INPUT_EMAIL_LOG_TO_YOU_ACCOUNT, email)

    def input_password_log_to_your_account(self, password):
        """Вводит пароль на форме входа на главной странице."""
        self.input_text(self._INPUT_PASSWORD_LOG_TO_YOU_ACCOUNT, password)

    def click_log_to_account(self):
        """Кликает по кнопке 'Войти' на форме входа на главной странице и проверяет успешный вход."""
        self.click_element(self._BUTTON_LOG_TO_ACCOUNT)
        assert self.driver.current_url == self._links["HOST"], f"Ожидался переход на главную после входа, но URL: {self.driver.current_url}"

    def open(self):
        """Открывает главную страницу."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть главную страницу: {self.driver.current_url}"