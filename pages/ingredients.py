from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage

class IngredientsPage(BasePage):
    """Работа с разделами ингредиентов."""

    _login_path = "login"
    _email = (By.XPATH, "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _password = (By.XPATH, "//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _login_btn = (By.XPATH, "//button[contains(@class, 'button_button__33qZ0') and contains(@class, 'button_button_type_primary__1O7Bx') and contains(@class, 'button_button_size_medium__3zxIa')]")
    _sauces_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Соусы']")
    _fillings_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Начинки']")
    _buns_tab = (By.XPATH, "//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'pt-4') and contains(@class, 'pr-10') and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Булки']")

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
        self.click(self._login_btn)

    def go_to_sauces(self):
        """Перейти к разделу 'Соусы'."""
        self.click(self._sauces_tab)

    def go_to_fillings(self):
        """Перейти к разделу 'Начинки'."""
        self.click(self._fillings_tab)

    def go_to_buns(self):
        """Перейти к разделу 'Булки'."""
        self.click(self._buns_tab)

    def check_tabs(self):
        """Проверить, что все вкладки активируются."""
        assert self.is_tab_active('Соусы'), "Вкладка 'Соусы' не активна"
        assert self.is_tab_active('Начинки'), "Вкладка 'Начинки' не активна"
        assert self.is_tab_active('Булки'), "Вкладка 'Булки' не активна"

    def is_tab_active(self, tab_name):
        """Проверить, что вкладка активна."""
        xpath = f"//span[text()='{tab_name}' and contains(@class, 'tab_tab_type_current__2BEPc')]"
        try:
            self.find((By.XPATH, xpath))
            return True
        except NoSuchElementException:
            return False
