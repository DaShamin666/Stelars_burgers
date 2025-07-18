from base.base_page import BasePage
from data.links import Links
# Вход через кнопку в форме регистрации
class SignInRegistrationPage(BasePage):

    _PAGE_URL = Links.REGISTER
    _BUTTON_SIGN_IN = ("xpath","//a[contains(@class, 'Auth_link__1fOlj') and text()='Войти']")
    _INPUT_EMAIL = ("xpath","//input[contains(@class, 'text input__textfield text_type_main-default')"
                            " and @name='name']")
    _INPUT_PASSWIRD = ("xpath","//input[contains(@class, 'text input__textfield text_type_main-default')"
                               " and @type='password' and @name='Пароль']")
    _CLICK_BUTTON_SIGN_IN = ('xpath',"//button[contains(@class, 'button_button__33qZ0')"
                                     " and contains(@class, 'button_button_type_primary__1O7Bx')"
                                     " and contains(@class, 'button_button_size_medium__3zxIa') and text()='Войти']")

    def click_button_profile_registration(self):
        self.click_element(self._BUTTON_SIGN_IN)

    def input_email_on_profile_registration(self, email):
        self.input_text(self._INPUT_EMAIL, email)

    def input_password_on_profile_registration(self, password):
        self.input_text(self._INPUT_PASSWIRD, password)

    def click_button_on_profile_registration_two(self):
        self.click_element(self._CLICK_BUTTON_SIGN_IN)