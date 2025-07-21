from dataclasses import dataclass


@dataclass
class UserCredentials:
    username: str
    password: str
    email: str


# Пользователи для разных окружений
USERS = {
    "dev_user1": UserCredentials("dev_user1", "Qwerty-12345!", "dev_user1@example.com"),
    "dev_user2": UserCredentials(
        "dev_user2", "Qwerty-12345!!", "dev_user2@example.com"
    ),
    "stage_user1": UserCredentials(
        "stage_user1", "stagepass1", "stage_user1@example.com"
    ),
    "stage_user2": UserCredentials(
        "stage_user2", "stagepass2", "stage_user2@example.com"
    ),
}


@dataclass
class EnvironmentConfig:
    url: str
    default_user: str


# Окружения
ENVIRONMENTS = {
    "DEV": EnvironmentConfig(
        url="https://stellarburgers.nomoreparties.site/", default_user="dev_user1"
    ),
    "STAGE": EnvironmentConfig(
        url="https://stage.stellarburgers.nomoreparties.site/",
        default_user="stage_user1",
    ),
}


def get_env_config(env_name: str):
    return ENVIRONMENTS[env_name.upper()]


def get_user(user_name: str):
    return USERS[user_name]
