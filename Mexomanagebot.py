import asyncio
import logging
import config
import sqlite3
import pogoda

from aiogram import Bot,Dispatcher,executor,types
import keyboards as kb

from aiogram.dispatcher.filters import BoundFilter
API_TOKEN=config.API_TOKEN
bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)


loop = asyncio.get_event_loop()  #бот в режиме ожидания 
delay = 10                    #будет функция далее;  -ВРЕМЯ ОЖИДАНИЯ БОТА


conn=sqlite3.connect('db.db')
cursor=conn.cursor()
@dp.message_handler(commands=['start'])
async def new_user(message):
    us_id=message.from_user.id
    result= cursor.execute('SELECT * FROM "test" WHERE "user_id"=?', (us_id,)).fetchall()
    if bool(len(result))==True:
                           sticker_hi=open('6.png','rb')
                           await bot.send_sticker(message.chat.id, sticker_hi )
                           await bot.send_message(message.chat.id,'Добро пожаловать, хозяин, рада вас видеть :3',
                           reply_markup=kb.kb_test)

    else:
            sticker_reg=open('2.png','rb')
            name=message.from_user.first_name
            await bot.send_sticker(message.chat.id, sticker_reg)
            await bot.send_message(message.chat.id, 'Здравствуй, '+name+', приятно познакомится, я-MexoBot, надеюсь мы с тобой поладим :)')
            cursor.execute("INSERT INTO test (user_id) VALUES (?)", (message.from_user.id,))
            conn.commit()

@dp.message_handler()
async def weather(message: types.Message):
    if message.text=='Погода':
        await bot.send_message(message.chat.id,' Температура в Алнашах ожидается завтра '+str(pogoda.temp_next_day)+pogoda.day)
    elif message.text.lower()=='спасибо':
        sticker=open('thanks.png','rb')
        await bot.send_sticker(message.chat.id, sticker)
    else:
        sticker=open('dont_understand.png','rb')
        await bot.send_sticker(message.chat.id, sticker)
    async def my_func():
        await bot.send_message(message.chat.id, 'Проверка') #тут удали если не работает
        when_to_call = loop.time() + delay 
        loop.call_at(when_to_call, my_callback)

    def my_callback():
        asyncio.ensure_future(my_func())


        
    




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)