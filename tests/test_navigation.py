import pytest
import allure


@allure.feature("Навигация и переходы")
class TestNavigation:
    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверка перехода по клику на «Личный кабинет»")
    def test_profile_navigation(self, login_profile_page, user):
        with allure.step("Открываем главную страницу"):
            login_profile_page.open()
        with allure.step("Переходим по кнопке 'Личный кабинет'"):
            login_profile_page.open_login()
        with allure.step("Проверяем, что открыта страница логина"):
            login_profile_page.url_contains("login")

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверка перехода по клику на «Конструктор» и на логотип Stellar Burgers")
    def test_constructor_and_logo_navigation(self, navigation_page):
        with allure.step("Открываем страницу логина"):
            navigation_page.open_login()
        with allure.step("Кликаем по логотипу Stellar Burgers"):
            navigation_page.click_logo()
        with allure.step("Проверяем переход на главную страницу"):
            navigation_page.check_main_opened()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверка выхода по кнопке «Выйти» в личном кабинете")
    def test_logout(self, profile_exit_page, user):
        with allure.step("Открываем страницу авторизации"):
            profile_exit_page.open_login()
        with allure.step("Выполняем вход"):
            profile_exit_page.sign_in(user.email, user.password)
        with allure.step("Переходим в личный кабинет"):
            profile_exit_page.go_to_profile()
        with allure.step("Нажимаем 'Выйти'"):
            profile_exit_page.logout()
        with allure.step("Проверяем успешный выход"):
            profile_exit_page.check_logout()

    @pytest.mark.smoke
    @pytest.mark.regression
    @allure.title("Проверка что работают переходы к разделам: «Булки», «Соусы», «Начинки»")
    def test_ingredients_sections(self, ingredients_page, user):
        with allure.step("Открываем страницу авторизации"):
            ingredients_page.open_login()
        with allure.step("Выполняем вход"):
            ingredients_page.sign_in(user.email, user.password)
        with allure.step("Переходим к разделу 'Соусы'"):
            ingredients_page.go_to_sauces()
        with allure.step("Переходим к разделу 'Начинки'"):
            ingredients_page.go_to_fillings()
        with allure.step("Переходим к разделу 'Булки'"):
            ingredients_page.go_to_buns()
        with allure.step("Проверяем корректность навигации по вкладкам"):
            ingredients_page.check_tabs()
