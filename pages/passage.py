from pages.base_page import BasePage

class Passage(BasePage):
    def __init__(self, driver, links):
        super().__init__(driver)
        self._links = links
        self._PAGE_URL = links["LOGIN"]

    _BUTTON_STELARS_BURGERS = ("xpath",'//*[@id="root"]/div/header/nav/div')

    def click_stellar_burgers_logo(self):
        """Кликает по логотипу Stellar Burgers в хедере и проверяет переход на главную страницу."""
        self.click_element(self._BUTTON_STELARS_BURGERS)
        assert self.driver.current_url == self._links["HOST"], f"Ожидался переход на главную после клика по логотипу, но URL: {self.driver.current_url}"

    def open(self):
        """Открывает страницу логина."""
        self.driver.get(self._PAGE_URL)
        assert self.driver.current_url == self._PAGE_URL, f"Не удалось открыть страницу логина: {self.driver.current_url}"