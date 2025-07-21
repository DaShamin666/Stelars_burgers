from pages.base_page import BasePage

class SignInPasswordRecoveryPage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["LOGIN"]

    _BUTTON_RECOVERY_PASSWORD = ('xpath',"//a[contains(@class, 'Auth_link__1fOlj') and text()='Восстановить пароль']")
    _EMAIL_RECOVERY_INPUT = ('xpath',"//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _BUTTON_RECOVERY = ('xpath',"//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa') and text()='Восстановить']")

    def click_button_recovery_password(self):
        """Кликает по ссылке 'Восстановить пароль'."""
        self.click_element(self._BUTTON_RECOVERY_PASSWORD)

    def input_email_recovery(self, email):
        """Вводит email для восстановления пароля."""
        self.input_text(self._EMAIL_RECOVERY_INPUT, email)

    def click_button_recovery(self):
        """Кликает по кнопке 'Восстановить' после ввода email. (Можно добавить assert на успешное восстановление)"""
        self.click_element(self._BUTTON_RECOVERY)
        # assert ... (например, assert self.is_recovery_successful())

    def open(self):
        """Открывает страницу восстановления пароля."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу восстановления пароля: {self.driver.current_url}"