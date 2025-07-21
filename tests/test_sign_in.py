import pytest
import allure


@allure.feature("Авторизация")
class TestSignIn:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_sign_in_from_main(self, login_main_page, user):
        with allure.step("Открываем главную страницу"):
            login_main_page.open()
        with allure.step("Выполняем вход через главную страницу"):
            login_main_page.sign_in_from_main(user.email, user.password)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку «Личный кабинет»")
    def test_sign_in_via_profile(self, login_profile_page, user):
        with allure.step("Открываем главную страницу"):
            login_profile_page.open()
        with allure.step("Выполняем вход через 'Личный кабинет'"):
            login_profile_page.sign_in_via_profile(user.email, user.password)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме регистрации")
    def test_sign_in_from_registration(self, login_registration_page, user):
        with allure.step("Открываем страницу регистрации"):
            login_registration_page.open()
        with allure.step("Выполняем вход через форму регистрации"):
            login_registration_page.sign_in_from_registration(user.email, user.password)

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме восстановления пароля")
    def test_sign_in_from_recovery(self, login_recovery_page, user):
        with allure.step("Открываем страницу восстановления пароля"):
            login_recovery_page.open()
        with allure.step("Выполняем вход через восстановление пароля"):
            login_recovery_page.sign_in_from_recovery(user.email, user.password)
