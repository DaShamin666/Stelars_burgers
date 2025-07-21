import pytest
import allure

@allure.feature("Тесты для входа пользователя")
class TestSign:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку Личный кабинет")
    def test_sign(self, sign_in_page, dev_user):
        with allure.step("открываем домашнюю страницу"):
            sign_in_page.open()
        with allure.step("нажимаем кнопку личного кабинета"):
            sign_in_page.click_button_on_sign_in_profile()
        with allure.step("вводим почту"):
            sign_in_page.input_email_on_sign_in(dev_user.email)
        with allure.step("вводим пароль"):
            sign_in_page.input_password_on_sign_in(dev_user.password)
        with allure.step("нажимаем кнопку входа"):
            sign_in_page.click_button_on_sign()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме регистрации")
    def test_sign_in_button_on_registration(self, sign_in_profile_registration, dev_user):
        with allure.step("открываем домашнюю страницу регистрации"):
            sign_in_profile_registration.open()
        with allure.step("нажимаем кнопку войти в форме регистрации"):
            sign_in_profile_registration.click_button_profile_registration()
        with allure.step("вводим почту"):
            sign_in_profile_registration.input_email_on_profile_registration(dev_user.email)
        with allure.step("вводим пароль"):
            sign_in_profile_registration.input_password_on_profile_registration(dev_user.password)
        with allure.step("нажимаем кнопку входа"):
            sign_in_profile_registration.click_button_on_profile_registration_two()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход через кнопку в форме восстановления пароля")
    def test_sign_in_password_recovery(self, sign_in_password_recovery, dev_user):
        with allure.step("открываем страницу авторизации"):
            sign_in_password_recovery.open()
        with allure.step("нажимаем кнопку восстановления пароля"):
            sign_in_password_recovery.click_button_recovery_password()
        with allure.step("вводим почту профиля"):
            sign_in_password_recovery.input_email_recovery(dev_user.email)
        with allure.step("нажимаем кнопку восстановить"):
            sign_in_password_recovery.click_button_recovery()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Вход по кнопке «Войти в аккаунт» на главной")
    def test_sign_in_to_your_account(self, log_in_to_your_account, dev_user):
        with allure.step("открываем главную страницу"):
            log_in_to_your_account.open()
        with allure.step("нажимаем кнопку войти в аккаунт"):
            log_in_to_your_account.click_log_in_to_your_account()
        with allure.step("вводим почту профиля"):
            log_in_to_your_account.input_email_log_to_your_account(dev_user.email)
        with allure.step("вводим пароль профиля"):
            log_in_to_your_account.input_password_log_to_your_account(dev_user.password)
        with allure.step("нажимаем кнопку входа"):
            log_in_to_your_account.click_log_to_account()

