from dataclasses import dataclass

from environs import Env

channels = ["-1001984514257"]

admins = [
    1684537746,
]
@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        db=DbConfig(
            host='127.0.0.1',
            # host=env.str('DB_HOST'),
            # password=env.str('DB_PASS'),
            password='12345',
            # user=env.str('DB_USER'),
            user='tester',
            database='tester'
            # database=env.str('DB_NAME')
        ),
        misc=Miscellaneous()
    )
