from base.base_page import BasePage
from data.links import Links



class LogInToYourAccountPage(BasePage):
    _PAGE_URL = Links.HOST
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
        self.click_element(self._BUTTON_LOG_TO_YOU_ACCOUNT)

    def input_email_log_to_your_account(self,email):
        self.input_text(self._INPUT_EMAIL_LOG_TO_YOU_ACCOUNT,email)

    def input_password_log_to_your_account(self,password):
        self.input_text(self._INPUT_PASSWORD_LOG_TO_YOU_ACCOUNT,password)

    def click_log_to_account(self):
        self.click_element(self._BUTTON_LOG_TO_ACCOUNT)