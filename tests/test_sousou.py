



from config.environments import get_env_config, get_user
import pytest
import allure
from base.base_test import BaseTest

class TestTransition(BaseTest):
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers")
    def test_stellar_burgers_logo(self):
        with allure.step("открываем cтраницу логина"):
            self.passage.open()
        with allure.step("переходим по логитипу Stellar Burgers"):
            self.passage.click_stellar_burgers_logo()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("выход по кнопке «Выйти» в личном кабинете")
    def test_exit_in_profile(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем страницу авторизации"):
            self.exit_in_profile.open()
        with allure.step("вводим почту"):
            self.exit_in_profile.input_email_on_exit(user.email)
        with allure.step("вводим пароль"):
            self.exit_in_profile.input_password_on_exit(user.password)
        with allure.step("нажимаем кнопку войти"):
            self.exit_in_profile.click_button_sign_on_exit()
        with allure.step("нажимаем кнопку личного профиля"):
            self.exit_in_profile.click_button_profile_exit()
        with allure.step("нажимаем кнопку выйти"):
            self.exit_in_profile.click_button_exit()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("переходы к разделам:«Булки»,«Соусы»,«Начинки»")
    def test_buns_sauces_fillings_passages(self):
        env = get_env_config("DEV")
        user = get_user(env.default_user)
        with allure.step("открываем страницу авторизации"):
            self.buns_passages.open()
        with allure.step("вводим почту"):
            self.buns_passages.input_email_buns_sauces(user.email)
        with allure.step("вводим пароль"):
            self.buns_passages.input_password_buns_sauces(user.password)
        with allure.step("нажимаем кнопку войти"):
            self.buns_passages.click_button_buns_sauces()
        with allure.step("нажимаем кнопку «Соусы»"):
            self.buns_passages.click_button_sauces()
        with allure.step("нажимаем кнопку «Начинки»"):
            self.buns_passages.click_button_fillings()
        with allure.step("нажимаем кнопку «Булки»"):
            self.buns_passages.click_button_buns()







