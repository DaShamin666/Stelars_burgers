from base.base_page import BasePage
from data.links import Links



class RegistrationPage(BasePage):
    # Локаторы элементов

    _NAME_FIELD = ("xpath","//input[contains(@class, 'input__textfield') and @name='name' and @type='text']")
    _EMAIL_FIELD = ("xpath", "//div[contains(@class, 'input_type_text')]//label[text()='Email']/following-sibling::input[@type='text']")
    _PASSWORD_FIELD = ("xpath","//input[contains(@class, 'input__textfield') and @type='password' and @name='Пароль']")
    _BUTTON_FIELD = ("xpath","//button[contains(@class, 'button_button') and text()='Зарегистрироваться']")
    _INPUT_EMAIL_SIGN_IN = ("xpath","//input[@class='text input__textfield text_type_main-default' and @name='name']")
    _INPUT_PASSWORD_SIGN_IN = ("xpath",
                               "//input[@class='text input__textfield text_type_main-default' and @type='password'"
                               " and @name='Пароль']")
    _PAGE_URL = Links.REGISTER
    _BUTTON_FIELD_IN_SIGN_IN = ("xpath","//button[contains(@class, 'button_button__33qZ0')"
                                " and contains(@class,"
                                " 'button_button_type_primary__1O7Bx')"
                                " and contains(@class, 'button_button_size_medium__3zxIa')]")


    def input_name(self,name):
        self.input_text(self._NAME_FIELD, name)

    def input_email(self,email):
        self.input_text(self._EMAIL_FIELD, email)

    def input_password(self,password):
        self.input_text(self._PASSWORD_FIELD, password)

    def click_button(self):
        self.click_element(self._BUTTON_FIELD)

    def input_email_on_login(self,email):
        self.input_text(self._INPUT_EMAIL_SIGN_IN, email)

    def input_password_on_login(self,password):
        self.input_text(self._INPUT_PASSWORD_SIGN_IN,password)

    def click_button_on_sign_in(self):
        self.click_element(self._BUTTON_FIELD_IN_SIGN_IN)

    def is_registration_successful(self):
        expected_url = Links.HOST
        return self.driver.current_url == expected_url

    def is_registration_not_sucsess(self):
        expected_url = Links.REGISTER
        return self.driver.current_url == expected_url