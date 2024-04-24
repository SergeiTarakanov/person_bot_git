import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage2

from tgbot.config import load_config
# from tgbot.filters.admin import AdminFilter
# from tgbot.filters.forwarded_message import IsForwarded
# from tgbot.filters.private_chat import IsPrivate


from tgbot.handlers.users.add_info import register_add_db

# from tgbot.handlers.error_handler import error_handler


from tgbot.handlers.users.start import register_start

# from tgbot.middlewares.big_brother import BigBrather
# from tgbot.middlewares.environment import EnvironmentMiddleware
# from tgbot.middlewares.trottling import ThrottlingMiddleware
# from tgbot.misc.utils.set_bot_commands import set_default_commands

logger = logging.getLogger(__name__)


# def register_all_middlewares(dp, config):
    # dp.setup_middleware(EnvironmentMiddleware(config=config))
    # dp.setup_middleware(BigBrather())
    # dp.setup_middleware(ThrottlingMiddleware())
# def register_all_filters(dp):
    # dp.filters_factory.bind(AdminFilter)
    # dp.filters_factory.bind(IsPrivate)
    # dp.filters_factory.bind(IsForwarded)
def register_all_handlers(dp):
    register_add_db(dp)
    register_start(dp)



async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")
    config = load_config(".env")

    storage = RedisStorage2() if config.tg_bot.use_redis else MemoryStorage()
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=storage)

    bot['config'] = config

    # register_all_middlewares(dp, config)
    # register_all_filters(dp)
    register_all_handlers(dp)

    # start
    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
