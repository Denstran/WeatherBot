from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

cb = CallbackData('report', 'city')

city_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Москва', callback_data='report:moscow'),
            InlineKeyboardButton('Санкт-Петербург', callback_data='report:saint petersburg')
        ],
        [
            InlineKeyboardButton('Самара', callback_data='report:samara'),
            InlineKeyboardButton('Новосибирск', callback_data='report:novosibirsk')
        ],
        [
            InlineKeyboardButton('Екатеринбург', callback_data='report:yekaterinburg'),
            InlineKeyboardButton('Казань', callback_data='report:kazan')
        ]
    ]
)