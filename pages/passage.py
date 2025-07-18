from base.base_page import BasePage
from data.links import Links
# Проверь переход по клику на «Личный кабинет»

class Passage(BasePage):
    _PAGE_URL = Links.LOGIN
    _BUTTON_STELARS_BURGERS = ("xpath",'//*[@id="root"]/div/header/nav/div')

    def click_stellar_burgers_logo(self):
        self.click_element(self._BUTTON_STELARS_BURGERS)