from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage
from pages.sign_in_button_in_registration import SignInRegistrationPage
from pages.sign_in_profile_button import SignIn
from pages.sign_in_password_recovery import SignInPasswordRecoveryPage
from pages.passage import Passage
from pages.sign_in_to_your_account import LogInToYourAccountPage
from pages.exit_in_profile import ExitInProfile
from pages.buns_sauces_fillings_passages import BunsSauceFillingsPassagesPage
import allure

class BasePage:
    """Базовый класс для всех страниц"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.registration_page = RegistrationPage(self.driver)
        self.sign_in = SignIn(self.driver)
        self.sign_in_profile_registration = SignInRegistrationPage(self.driver)
        self.sign_in_password_recovery = SignInPasswordRecoveryPage(self.driver)
        self.log_in_to_your_account = LogInToYourAccountPage(self.driver)
        self.passage = Passage(self.driver)
        self.exit_in_profile = ExitInProfile(self.driver)
        self.buns_passages = BunsSauceFillingsPassagesPage(self.driver)

    def find_element(self, locator):
        """Найти элемент с явным ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """Нажать на элемент с явным ожиданием кликабельности"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def input_text(self, locator, text):
        """Ввести текст в элемент"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def check_url(self, url):
        """Проверка URL после авторизации"""
        assert self.driver.current_url == url, f"URL не соответствует ожидаемому: {url}"

    def attach_screenshot(self, name="screenshot"):
        """Сделать скриншот и прикрепить к отчету Allure."""
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )