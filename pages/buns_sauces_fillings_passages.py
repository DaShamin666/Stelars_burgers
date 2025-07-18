from base.base_page import BasePage
from data.links import Links

class BunsSauceFillingsPassagesPage(BasePage):
    _PAGE_URL = Links.LOGIN
    _EMAIL_BUNS_SAUCES_FILLINGS = ("xpath", "//div[contains(@class, 'input_type_text')]//label[text()='Email']"
                             "/following-sibling::input[@type='text']")
    _PASSWORD_BUNS_SAUCES_FILLINGS = ("xpath","//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _BUTTON_BUNS_SAUCES_FILLINGS = ("xpath","//button[contains(@class, 'button_button__33qZ0')"
                                    " and contains(@class, 'button_button_type_primary__1O7Bx')"
                                    " and contains(@class, 'button_button_size_medium__3zxIa')]")
    _BUTTON_SAUCES = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')"
                               " and contains(@class, 'pt-4') and contains(@class, 'pr-10')"
                               " and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Соусы']")
    _BUTTON_FILLINGS = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')"
                                 " and contains(@class, 'pt-4') and contains(@class, 'pr-10')"
                                 " and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Начинки']")
    _BUTTON_BUNS = ("xpath", "//div[contains(@class, 'tab_tab__1SPyG')"
                             " and contains(@class, 'pt-4') and contains(@class, 'pr-10')"
                             " and contains(@class, 'pb-4') and contains(@class, 'pl-10')]//span[text()='Булки']")

    def input_email_buns_sauces(self, email):
        self.input_text(self._EMAIL_BUNS_SAUCES_FILLINGS,email)

    def input_password_buns_sauces(self, password):
        self.input_text(self._EMAIL_BUNS_SAUCES_FILLINGS,password)

    def click_button_buns_sauces(self):
        self.click_element(self._BUTTON_BUNS_SAUCES_FILLINGS)

    def click_button_sauces(self):
        self.click_element(self._BUTTON_SAUCES)

    def click_button_fillings(self):
        self.click_element(self._BUTTON_FILLINGS)

    def click_button_buns(self):
        self.click_element(self._BUTTON_BUNS)
