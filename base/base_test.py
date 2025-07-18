from pages.registration_page import RegistrationPage
from pages.sign_in_profile_button import SignIn
from pages.sign_in_button_in_registration import SignInRegistrationPage
from pages.sign_in_password_recovery import SignInPasswordRecoveryPage
from pages.sign_in_to_your_account import LogInToYourAccountPage
from pages.passage import Passage
from pages.exit_in_profile import ExitInProfile
from pages.buns_sauces_fillings_passages import BunsSauceFillingsPassagesPage

class BaseTest:

    def setup_method(self):
        self.registration_page = RegistrationPage(self.driver)
        self.sign_in = SignIn(self.driver)
        self.sign_in_profile_registration = SignInRegistrationPage(self.driver)
        self.sign_in_password_recovery = SignInPasswordRecoveryPage(self.driver)
        self.log_in_to_your_account = LogInToYourAccountPage(self.driver)
        self.passage = Passage(self.driver)
        self.exit_in_profile = ExitInProfile(self.driver)
        self.buns_passages = BunsSauceFillingsPassagesPage(self.driver)
