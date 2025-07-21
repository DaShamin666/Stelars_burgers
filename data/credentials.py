from faker import Faker
import json
import os


class Credentials:
    fake = Faker()
    USERS_DIR = os.path.dirname(os.path.abspath(__file__))
    DEFAULT_USER_FILE = os.path.join(USERS_DIR, "last_user.json")

    def generate_user(self):
        """Генерирует случайного пользователя."""
        return {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(length=12),
        }

    def save_user(self, user, filename=DEFAULT_USER_FILE):
        """Сохраняет пользователя в JSON-файл."""
        with open(filename, "w") as f:
            json.dump(user, f)

    def load_user(self, filename=DEFAULT_USER_FILE):
        """Загружает пользователя из JSON-файла."""
        with open(filename, "r") as f:
            return json.load(f)
