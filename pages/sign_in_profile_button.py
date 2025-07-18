from base.base_page import BasePage
from data.links import Links
# Вход через кнопку «Личный кабинет»

class SignIn(BasePage):
    _PAGE_URL = Links.HOST
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
        self.click_element(self._BUTTON_PROFILE)

    def input_email_on_sign_in(self,email):
        self.input_text(self._INPUT_EMAIL_SIGN_IN, email)

    def input_password_on_sign_in(self,password):
        self.input_text(self._INPUT_PASSWORD_SIGN_IN, password)

    def click_button_on_sign(self):
        self.click_element(self._BUTTON_FIELD_SIGN_IN)


