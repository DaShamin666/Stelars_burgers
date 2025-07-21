from pages.base_page import BasePage

class BunsSauceFillingsPassagesPage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["LOGIN"]

    _EMAIL_BUNS_SAUCES_FILLINGS = ("xpath", "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _PASSWORD_BUNS_SAUCES_FILLINGS = ("xpath","//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _BUTTON_BUNS_SAUCES_FILLINGS = ("xpath","//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")
    _BUTTON_SAUCES = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Соусы']")
    _BUTTON_FILLINGS = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Начинки']")
    _BUTTON_BUNS = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Булки']")

    def open(self):
        """Открывает страницу авторизации."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу авторизации: {self.driver.current_url}"

    def input_email_buns_sauces(self, email):
        """Вводит email на странице переходов по разделам."""
        self.input_text(self._EMAIL_BUNS_SAUCES_FILLINGS, email)

    def input_password_buns_sauces(self, password):
        """Вводит пароль на странице переходов по разделам."""
        self.input_text(self._EMAIL_BUNS_SAUCES_FILLINGS, password)

    def click_button_buns_sauces(self):
        """Кликает по кнопке входа на странице переходов по разделам."""
        self.click_element(self._BUTTON_BUNS_SAUCES_FILLINGS)

    def is_tab_active(self, tab_name):
        """Проверяет, что вкладка с заданным именем активна."""
        active_tab_xpath = f"//span[text()='{tab_name}' and contains(@class, 'tab_tab_type_current__2BEPc')]"
        try:
            self.find_element(("xpath", active_tab_xpath))
            return True
        except Exception:
            return False

    def click_button_sauces(self):
        """Кликает по вкладке 'Соусы' и проверяет, что вкладка активна."""
        self.click_element(self._BUTTON_SAUCES)
        assert self.is_tab_active('Соусы'), "Вкладка 'Соусы' не стала активной после клика"

    def click_button_fillings(self):
        """Кликает по вкладке 'Начинки' и проверяет, что вкладка активна."""
        self.click_element(self._BUTTON_FILLINGS)
        assert self.is_tab_active('Начинки'), "Вкладка 'Начинки' не стала активной после клика"

    def click_button_buns(self):
        """Кликает по вкладке 'Булки' и проверяет, что вкладка активна."""
        self.click_element(self._BUTTON_BUNS)
        assert self.is_tab_active('Булки'), "Вкладка 'Булки' не стала активной после клика"
