import os
import logging
import time

from dotenv import load_dotenv
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from api.model import search_image
from api.utils.static_text import START, INFO, INPUT_ERROR

# Логирование
logging.basicConfig(filename='log.log',
                    level=logging.INFO)

# Загрузка токена через env
load_dotenv()
TOKEN = os.getenv('TOKEN')

# Инициализация бота
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    logging.info(f'{user_id} запустил бота в {time.asctime()}')
    await message.reply(START % user_name, parse_mode='Markdown')


@dp.message_handler(commands=['info'])
async def process_help_command(message: types.Message):
    await message.reply(INFO)


@dp.message_handler()
async def echo_message(message: types.Message):
    txt = message.text
    user_id = message.from_user.id
    user_name = message.from_user.full_name
    if len(txt) > 18:
        await bot.send_message(user_id, 'Пришлите текст длиной не более 18 символов')
    else:
        logging.info(f'Нам написал {user_name} в {time.asctime()}, его id = {user_id}')
        await bot.send_photo(user_id, search_image(txt))


# обработчик на случай, если был прислан не текст, а стикер, фото или любой другой тип данных
@dp.message_handler(content_types='any')
async def unknown_message(message: types.Message):
    user_id = message.from_user.id
    await bot.send_message(user_id, INPUT_ERROR)

if __name__ == '__main__':
    executor.start_polling(dp)
