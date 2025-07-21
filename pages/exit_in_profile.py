from pages.base_page import BasePage

class ExitInProfile(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["LOGIN"]

    _EMAIL_FIELD_ON_EXIT = ("xpath", "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _PASSWORD_FIELD_ON_EXIT = ("xpath","//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _BUTTON_SIGN_ON_EXIT = ("xpath","//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")
    _BUTTON_PROFILE = ("xpath","//a[contains(@class, 'AppHeader_header__link__3D_hX') and contains(., 'Личный Кабинет')]")
    _BUTTON_EXIT = ("xpath","//button[contains(@class, 'Account_button__14Yp3') and contains(@class, 'text') and contains(@class, 'text_type_main-medium') and contains(@class, 'text_color_inactive') and text()='Выход']")

    def input_email_on_exit(self, email):
        """Вводит email на странице выхода из профиля."""
        self.input_text(self._EMAIL_FIELD_ON_EXIT, email)

    def input_password_on_exit(self, password):
        """Вводит пароль на странице выхода из профиля."""
        self.input_text(self._EMAIL_FIELD_ON_EXIT, password)

    def click_button_sign_on_exit(self):
        """Кликает по кнопке входа на странице выхода из профиля."""
        self.click_element(self._BUTTON_SIGN_ON_EXIT)

    def click_button_profile_exit(self):
        """Кликает по кнопке 'Личный кабинет' в профиле пользователя."""
        self.click_element(self._BUTTON_PROFILE)

    def click_button_exit(self):
        """Кликает по кнопке 'Выход' в профиле пользователя и проверяет успешный выход."""
        self.click_element(self._BUTTON_EXIT)
        assert self.driver.current_url == self._PAGE_URL, f"Ожидался переход на страницу логина после выхода, но URL: {self.driver.current_url}"

    def open(self):
        """Открывает страницу авторизации."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу авторизации: {self.driver.current_url}"

