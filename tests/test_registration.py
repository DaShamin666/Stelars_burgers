import pytest
import allure
from base.base_test import BaseTest
from data.credentials import Credentials


@allure.feature("Тесты для регистрации пользователя")
class TestRegistration(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Создание профиля пользователя")
    def test_registration(self):
        user = Credentials().generate_user()
        with allure.step("открываем страницу регистрации"):
            self.registration_page.open()
        with allure.step("вводим имя"):
            self.registration_page.input_name(user['username'])
        with allure.step("вводим почту"):
            self.registration_page.input_email(user['email'])
        with allure.step("вводим пароль"):
            self.registration_page.input_password(user['password'])
        with allure.step("нажимаем кнопку регистрации"):
            self.registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            self.registration_page.input_email_on_login(user['email'])
        with allure.step("вводим пароль на странице входа"):
            self.registration_page.input_password_on_login(user['password'])
        with allure.step("нажимаем кнопку входа"):
            self.registration_page.click_button_on_sign_in()
        with allure.step("проверяем что вошли на домашнюю страницу"):
            self.registration_page.is_registration_successful()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректное имя")
    def test_registration_invalid_name(self):
        user = Credentials().generate_user()
        invalid_name = "!"
        with allure.step("Открываем страницу регистрации"):
            self.registration_page.open()
        with allure.step("Вводим некорректное имя"):
            self.registration_page.input_name(invalid_name)
        with allure.step("Вводим почту"):
            self.registration_page.input_email(user['email'])
        with allure.step("Вводим пароль"):
            self.registration_page.input_password(user['password'])
        with allure.step("Пробуем зарегистрироваться"):
            self.registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            self.registration_page.input_email_on_login(user['email'])
        with allure.step("вводим пароль на странице входа"):
            self.registration_page.input_password_on_login(user['password'])
        with allure.step("нажимаем кнопку входа"):
            self.registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert self.registration_page.is_registration_not_sucsess()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректный email")
    def test_registration_invalid_email(self):
        user = Credentials().generate_user()
        invalid_email = "not-an-email"
        with allure.step("Открываем страницу регистрации"):
            self.registration_page.open()
        with allure.step("Вводим имя"):
            self.registration_page.input_name(user['username'])
        with allure.step("Вводим некорректный email"):
            self.registration_page.input_email(invalid_email)
        with allure.step("Вводим пароль"):
            self.registration_page.input_password(user['password'])
        with allure.step("Пробуем зарегистрироваться"):
            self.registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            self.registration_page.input_email_on_login(user['email'])
        with allure.step("вводим пароль на странице входа"):
            self.registration_page.input_password_on_login(user['password'])
        with allure.step("нажимаем кнопку входа"):
            self.registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert self.registration_page.is_registration_not_sucsess()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректный пароль")
    def test_registration_invalid_password(self):
        user = Credentials().generate_user()
        invalid_password = "123"
        with allure.step("Открываем страницу регистрации"):
            self.registration_page.open()
        with allure.step("Вводим имя"):
            self.registration_page.input_name(user['username'])
        with allure.step("Вводим почту"):
            self.registration_page.input_email(user['email'])
        with allure.step("Вводим некорректный пароль"):
            self.registration_page.input_password(invalid_password)
        with allure.step("Пробуем зарегистрироваться"):
            self.registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            self.registration_page.input_email_on_login(user['email'])
        with allure.step("вводим пароль на странице входа"):
            self.registration_page.input_password_on_login(user['password'])
        with allure.step("нажимаем кнопку входа"):
            self.registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert self.registration_page.is_registration_not_sucsess()


