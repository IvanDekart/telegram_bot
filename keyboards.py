from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn_weather=KeyboardButton('Погода')
kb_test=ReplyKeyboardMarkup(resize_keyboard=True).add(btn_weather)