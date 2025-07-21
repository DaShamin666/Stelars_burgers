from config.environments import get_env_config, get_user
import pytest
import allure

class TestTransition:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers")
    def test_stellar_burgers_logo(self, passage):
        with allure.step("открываем cтраницу логина"):
            passage.open()
        with allure.step("переходим по логитипу Stellar Burgers"):
            passage.click_stellar_burgers_logo()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("выход по кнопке «Выйти» в личном кабинете")
    def test_exit_in_profile(self, exit_in_profile, dev_user):
        with allure.step("открываем страницу авторизации"):
            exit_in_profile.open()
        with allure.step("вводим почту"):
            exit_in_profile.input_email_on_exit(dev_user.email)
        with allure.step("вводим пароль"):
            exit_in_profile.input_password_on_exit(dev_user.password)
        with allure.step("нажимаем кнопку войти"):
            exit_in_profile.click_button_sign_on_exit()
        with allure.step("нажимаем кнопку личного профиля"):
            exit_in_profile.click_button_profile_exit()
        with allure.step("нажимаем кнопку выйти"):
            exit_in_profile.click_button_exit()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("переходы к разделам:«Булки»,«Соусы»,«Начинки»")
    def test_buns_sauces_fillings_passages(self, buns_passages, dev_user):
        with allure.step("открываем страницу авторизации"):
            buns_passages.open()
        with allure.step("вводим почту"):
            buns_passages.input_email_buns_sauces(dev_user.email)
        with allure.step("вводим пароль"):
            buns_passages.input_password_buns_sauces(dev_user.password)
        with allure.step("нажимаем кнопку войти"):
            buns_passages.click_button_buns_sauces()
        with allure.step("нажимаем кнопку «Соусы»"):
            buns_passages.click_button_sauces()
        with allure.step("нажимаем кнопку «Начинки»"):
            buns_passages.click_button_fillings()
        with allure.step("нажимаем кнопку «Булки»"):
            buns_passages.click_button_buns()







