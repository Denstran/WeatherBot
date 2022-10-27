from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery
from keyboards.cities_inlinekeyboard import city_keyboard, cb
from services.weather_service import get_weather
from config import Config

from bot import bot, dp


@dp.message_handler(Command('start'))
async def start(message: Message):
    await message.answer("Привет! Я бот, отвечающий за прогноз погоды!\n"
                         "Выбери город из списка, а я отправлю тебе прогноз!", reply_markup=city_keyboard)


@dp.callback_query_handler(cb.filter(city=['moscow', 'saint petersburg', 'samara', 'kazan', 'novosibirsk', 'yekaterinburg']))
async def weather_for_city(call: CallbackQuery, callback_data: dict):
    await call.message.answer(get_weather(callback_data.get('city'), Config.open_weather_token))
