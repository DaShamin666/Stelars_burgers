import pytest
import allure


@allure.feature("Тесты для регистрации пользователя")
class TestRegistration:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Создание профиля пользователя")
    def test_registration(self, registration_page, random_user):
        with allure.step("открываем страницу регистрации"):
            registration_page.open()
        with allure.step("вводим имя"):
            registration_page.input_name(random_user['username'])
        with allure.step("вводим почту"):
            registration_page.input_email(random_user['email'])
        with allure.step("вводим пароль"):
            registration_page.input_password(random_user['password'])
        with allure.step("нажимаем кнопку регистрации"):
            registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            registration_page.input_email_on_login(random_user['email'])
        with allure.step("вводим пароль на странице входа"):
            registration_page.input_password_on_login(random_user['password'])
        with allure.step("нажимаем кнопку входа"):
            registration_page.click_button_on_sign_in()
        with allure.step("проверяем что вошли на домашнюю страницу"):
            registration_page.is_registration_successful()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректное имя")
    def test_registration_invalid_name(self, registration_page, random_user):
        invalid_name = "!"
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим некорректное имя"):
            registration_page.input_name(invalid_name)
        with allure.step("Вводим почту"):
            registration_page.input_email(random_user['email'])
        with allure.step("Вводим пароль"):
            registration_page.input_password(random_user['password'])
        with allure.step("Пробуем зарегистрироваться"):
            registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            registration_page.input_email_on_login(random_user['email'])
        with allure.step("вводим пароль на странице входа"):
            registration_page.input_password_on_login(random_user['password'])
        with allure.step("нажимаем кнопку входа"):
            registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert registration_page.is_registration_not_sucsess()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректный email")
    def test_registration_invalid_email(self, registration_page, random_user):
        invalid_email = "not-an-email"
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим имя"):
            registration_page.input_name(random_user['username'])
        with allure.step("Вводим некорректный email"):
            registration_page.input_email(invalid_email)
        with allure.step("Вводим пароль"):
            registration_page.input_password(random_user['password'])
        with allure.step("Пробуем зарегистрироваться"):
            registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            registration_page.input_email_on_login(random_user['email'])
        with allure.step("вводим пароль на странице входа"):
            registration_page.input_password_on_login(random_user['password'])
        with allure.step("нажимаем кнопку входа"):
            registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert registration_page.is_registration_not_sucsess()

    @pytest.mark.regression
    @allure.title("Негативный тест: некорректный пароль")
    def test_registration_invalid_password(self, registration_page, random_user):
        invalid_password = "123"
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим имя"):
            registration_page.input_name(random_user['username'])
        with allure.step("Вводим почту"):
            registration_page.input_email(random_user['email'])
        with allure.step("Вводим некорректный пароль"):
            registration_page.input_password(invalid_password)
        with allure.step("Пробуем зарегистрироваться"):
            registration_page.click_button()
        with allure.step("вводим почту на странице входа"):
            registration_page.input_email_on_login(random_user['email'])
        with allure.step("вводим пароль на странице входа"):
            registration_page.input_password_on_login(random_user['password'])
        with allure.step("нажимаем кнопку входа"):
            registration_page.click_button_on_sign_in()
        with allure.step("Проверяем что остались на странице регистарции"):
            assert registration_page.is_registration_not_sucsess()


