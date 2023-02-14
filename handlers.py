from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from aiogram import types

from main import dp, bot
from config import admin_id, users2
from main import BotDB




@dp.message_handler(commands = "start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)

    await message.bot.send_message(message.from_user.id,"Вы подписались на рассылку!")

@dp.message_handler(Command('sendall'))
async def send_all(message: Message):
    if message.chat.id == admin_id:
        await message.answer('Start')
        for i in users2:
            await bot.send_message(i, message.text[message.text.find(''):])

        await message.answer('Done')

    else:
        await message.answer('Error')

@dp.message_handler(Command('sendallwp'))
async def send_all(message: Message):
    if message.chat.id == admin_id:
        await message.answer('Start')
        for i in users2:
            await bot.send_photo(i, open('laptop.jpg', 'rb'), message.text[message.text.find(' '):])

        await message.answer('Done')

    else:
        await message.answer('Error')
