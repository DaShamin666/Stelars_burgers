import pytest
import allure


@allure.feature("Регистрация")
class TestRegistration:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Успешная регистрация")
    def test_successful_registration(self, registration_page, random_user):
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Заполняем форму валидными данными"):
            registration_page.fill_form(
                random_user["username"], random_user["email"], random_user["password"]
            )
        with allure.step("Отправляем форму"):
            registration_page.submit()
        with allure.step("Входим с новыми данными"):
            registration_page.login_after_registration(
                random_user["email"], random_user["password"]
            )

    @pytest.mark.regression
    @allure.title("Негативный тест на поле 'Имя'")
    def test_invalid_name(self, registration_page, random_user):
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим некорректное имя"):
            registration_page.fill_form(
                "!", random_user["email"], random_user["password"]
            )
        with allure.step("Пытаемся зарегистрироваться"):
            registration_page.submit()
        with allure.step("Проверяем, что регистрация не удалась"):
            registration_page.check_failed()

    @pytest.mark.regression
    @allure.title("Негативный тест на поле 'Email'")
    def test_invalid_email(self, registration_page, random_user):
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим некорректный email"):
            registration_page.fill_form(
                random_user["username"], "not-an-email", random_user["password"]
            )
        with allure.step("Пытаемся зарегистрироваться"):
            registration_page.submit()
        with allure.step("Проверяем, что регистрация не удалась"):
            registration_page.check_failed()

    @pytest.mark.regression
    @allure.title("Тест на проверку ввода некорректного пароля")
    def test_invalid_password(self, registration_page, random_user):
        with allure.step("Открываем страницу регистрации"):
            registration_page.open()
        with allure.step("Вводим некорректный пароль"):
            registration_page.fill_form(
                random_user["username"], random_user["email"], "123"
            )
        with allure.step("Пытаемся зарегистрироваться"):
            registration_page.submit()
        with allure.step("Проверяем, что регистрация не удалась"):
            registration_page.check_failed()
