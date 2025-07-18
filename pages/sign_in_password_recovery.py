from base.base_page import BasePage
from data.links import Links

class SignInPasswordRecoveryPage(BasePage):
    _PAGE_URL = Links.LOGIN
    _BUTTON_RECOVERY_PASSWORD = ('xpath',"//a[contains(@class, 'Auth_link__1fOlj') and text()='Восстановить пароль']")
    _EMAIL_RECOVERY_INPUT = ('xpath',"//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _BUTTON_RECOVERY = ('xpath',"//button[contains(@class, 'button_button__33qZ0')"
                                " and contains(@class, 'button_button_type_primary__1O7Bx')"
                                " and contains(@class, 'button_button_size_medium__3zxIa') and text()='Восстановить']")

    def click_button_recovery_password(self):
        self.click_element(self._BUTTON_RECOVERY_PASSWORD)

    def input_email_recovery(self,email):
        self.input_text(self._EMAIL_RECOVERY_INPUT,email)

    def click_button_recovery(self):
        self.click_element(self._BUTTON_RECOVERY)