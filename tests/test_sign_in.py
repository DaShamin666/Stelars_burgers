import pytest
import allure
from base.base_test import BaseTest
from config.environments import get_env_config, get_user



@allure.feature("Тесты для входа пользователя")
class TestSign(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку Личный кабинет")
    def test_sign(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем домашнюю страницу"):
            self.sign_in.open()
        with allure.step("нажимаем кнопку личного кабинета"):
            self.sign_in.click_button_on_sign_in_profile()
        with allure.step("вводим почту"):
            self.sign_in.input_email_on_sign_in(user.email)
        with allure.step("вводим пароль"):
            self.sign_in.input_password_on_sign_in(user.password)
        with allure.step("нажимаем кнопку входа"):
            self.sign_in.click_button_on_sign()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме регистрации")
    def test_sign_in_button_on_registration(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем домашнюю страницу регистрации"):
            self.sign_in_profile_registration.open()
        with allure.step("нажимаем кнопку войти в форме регистрации"):
            self.sign_in_profile_registration.click_button_profile_registration()
        with allure.step("вводим почту"):
            self.sign_in_profile_registration.input_email_on_profile_registration(user.email)
        with allure.step("вводим пароль"):
            self.sign_in_profile_registration.input_password_on_profile_registration(user.password)
        with allure.step("нажимаем кнопку входа"):
            self.sign_in_profile_registration.click_button_on_profile_registration_two()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме восстановления пароля")
    def test_sign_in_password_recovery(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем страницу авторизации"):
            self.sign_in_password_recovery.open()
        with allure.step("нажимаем кнопку восстановления пароля"):
            self.sign_in_password_recovery.click_button_recovery_password()
        with allure.step("вводим почту профиля"):
            self.sign_in_password_recovery.input_email_recovery(user.email)
        with allure.step("нажимаем кнопку восстановить"):
            self.sign_in_password_recovery.click_button_recovery()
            #под авторизованным пользователем 500 ошибка,
            #если не авторизован то работает, но это ломает логику
            #восстановления пароля поэтому оставил тест так

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_sign_in_to_your_account(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем главную страницу"):
            self.log_in_to_your_account.open()
        with allure.step("нажимаем кнопку войти в аккаунт"):
            self.log_in_to_your_account.click_log_in_to_your_account()
        with allure.step("вводим почту профиля"):
            self.log_in_to_your_account.input_email_log_to_your_account(user.email)
        with allure.step("вводим пароль профиля"):
            self.log_in_to_your_account.input_password_log_to_your_account(user.password)
        with allure.step("нажимаем кнопку входа"):
            self.log_in_to_your_account.click_log_to_account()

    # @pytest.mark.smoke
    # @pytest.mark.regression
    # @allure.title("переход по клику на Личный кабинет")

