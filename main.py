from email import message
from lib2to3.pgen2 import token
import os
import rarfile
import shutil
import re
import requests
from datetime import datetime
import time
from aiogram import Dispatcher, executor
from aiogram.dispatcher.filters import ChatTypeFilter
from aiogram import Bot, types, executor
from aiogram.utils.markdown import hbold, hlink
import time
from threading import Timer
import asyncio
from aiogram.utils.exceptions import BadRequest
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext

TK = '5130191326:AAFcs52wD8Gni96j7XN2MYl6ugSjce7prmY'

class aki(StatesGroup):
    sms_text = State()


bot = Bot(token=TK, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)





@dp.message_handler(commands=['start'])
async def start(message: types.Message,  state: FSMContext):
    await message.answer("<b>Закинь список akaунтов....</b>")
    await aki.sms_text.set()


    @dp.message_handler(state=aki.sms_text)
    async def akaynti(message: types.Message,  state: FSMContext):

        chat_id = message.chat.id

                
               


        baza = []
        ww = message.text
        await message.delete()
        print("".join(map(str, ww)))
        url_pattern = r'https://[\S]+'
        u = re.findall(url_pattern, ww)
        s = len(u)
        #cislo = len(ww)
        await message.answer(f"<b>Подготавливаю {s} Акаунтов</b>")
        for x in u:
            async def sending_check(wait_for):
                while True:
                    await asyncio.sleep(wait_for)
                    nv = (datetime.now().strftime("%H:%M:%S"))
                    await message.answer(nv)
            os.system(f"curl -k -L --output temp_aka/telega.rar  {x}")
            time.sleep(4)
            rar_file = "temp_aka/telega.rar"
            dir_name = "data"
            rarobj = rarfile.RarFile(rar_file)
            rarobj.extractall(dir_name)
            xx = os.listdir(dir_name)
            await message.answer(f"<b>В работе {xx[0]} ожидайте....</b>")
            data_x = f"data/{xx[0]}"
            datax = os.listdir(data_x)
            os.system(f"powershell Remove-item data\{xx[0]}\{datax[0]} -recurse")
            os.system(f"powershell Remove-item data\{xx[0]}\{datax[1]} -recurse")
            os.system(f"powershell Remove-item data\{xx[0]}\{datax[3]} -recurse")
            os.system(f"powershell Remove-item data\{xx[0]}\\'{datax[4]}' -recurse")
            os.system(f"powershell copy  system/settingss data\{xx[0]}\\tdata\settingss")
            os.system(f"powershell copy  system/Telegram.exe data\{xx[0]}\\Telegram.exe")
            output_filename = f'akaunts_zip\{xx[0]}/'
            rar = f'akaunts_zip\{xx[0]}.zip'
            shutil.make_archive(output_filename, 'zip', data_x) 
            os.system(f"powershell Remove-item data\{xx[0]} -recurse")
            URL_TRANSFERSH = 'https://transfer.sh'
            with open(rar, 'rb') as data:
                conf_file = {rar: data}
                headers = {}
                r = requests.post(URL_TRANSFERSH, files=conf_file, headers=headers)
                d = r.text[19:]
                download_url = f"{URL_TRANSFERSH}/get{d}"
               # await message.answer(download_url)
                time.sleep(5)
                data.close()
                os.system(f"powershell Remove-item {rar} -recurse")
                baza.append(download_url)
                #loop = asyncio.get_event_loop()
                #loop.create_task(sending_check(2))
        await message.answer("<b>Готово</b>")
        xxx = '\n\n'.join(baza)
        await message.answer(
            f"<b>Вот список:</b>")
        await message.answer(
            f"{xxx}")
        baza.clear()
        await state.finish()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #loop.create_task(sending_check(2))
    executor.start_polling(dp)