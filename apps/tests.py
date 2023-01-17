from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '5874970015:AAH0NN1LEiZL2WKkUJP23UB2VZFvOYUH6uk'
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


@dp.message_handler(commands='start')
async def start_handler(message: types.Message):
    with open('save.txt', 'r') as file:
        await message.reply_document(document=file)


@dp.message_handler(commands='save')
async def start_handler(message: types.Message):
    text = message.text.replace('save', '')
    with open('save.txt', 'a') as file:
        file.write(text)
    await message.reply(f'{text} soz qoshildi')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
