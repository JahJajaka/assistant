import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
import requests
import json
from os import getenv
import Log

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = Log.get_logger()

# Initialize bot
bot = Bot(token=getenv('BOT_API_TOKEN'), parse_mode='HTML')
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command(commands=['start', 'help']))
async def send_welcome(message: Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi! I'm your personal assistant, ready to manage your data and help with all kinds of problems")

# Define states
class Form(StatesGroup):
    model_input = State()

@dp.message(Command(commands=['model']))
async def model_command(message: Message, state: FSMContext):
    """
    This handler will be called when user sends `/model` command
    """
    await message.reply("Please provide the input for the model:")
    await state.set_state(Form.model_input)

@dp.message(Form.model_input)
async def process_model_input(message: Message, state: FSMContext):
    """
    This handler will process the input provided after `/model` command
    """
    user_input = message.text
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'Connection': 'close'
    }

    payload = {
        "llm_model": f"{user_input}",
        "chat_id": f"{message.chat.id}"
    }
    response = requests.post(f'{getenv("APP_HOST")}:{getenv("APP_PORT")}/llm_model', headers=headers, data=json.dumps(payload)).json()
    await message.answer(response['message'])
    await state.clear()  # Clear the state

@dp.message()
async def answer(message: Message):
    headers = {
        "Accept": "application/json",
        'Content-Type': 'application/json',
        'Connection': 'close'
    }

    payload = {
        "event": f"{message.text}",
        "chat_id": f"{message.chat.id}"
    }
    response = requests.post(f'{getenv("APP_HOST")}:{getenv("APP_PORT")}{getenv("APP_ENDPOINT")}', headers=headers, data=json.dumps(payload)).json()
    await message.answer(response['message'])

async def main():
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.error(f"Error while getting updates. Error msg: {e}")
        logger.exception(e)

if __name__ == '__main__':
    logger.info('Bot started successfully')
    asyncio.run(main())