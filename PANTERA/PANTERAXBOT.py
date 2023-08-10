import requests
from aiogram import Dispatcher,types,Bot,executor
import logging
#from aiogram.utils.exceptions import BadRequest
# from APIS.INSTAGRAM import INSTAGRAM
import requests
from aiogram import Bot, Dispatcher, types, executor
import logging
# from APIS.INSTAGRAM import INSTAGRAM
from keyboardbuttons import button
from reqAPI import *
# from .states import *
from states import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext


# Telegram Bot API TOKEN (bu yerni o'zingizning botingizga tegishli TOKEN bilan almashtiring)
# API_TOKEN = '6633548961:AAGlr7mQ7efrFYXlQHm6nZgMLjNSF99bbwI'
API_TOKEN="5898677888:AAFVMeOLxI0A6oIkLUcS61rNKZ8C1XinEkw"
# Bot obyekti yaratish
bot = Bot(token=API_TOKEN,parse_mode="HTML")
dp = Dispatcher(bot,storage=MemoryStorage())

logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    # level=logging.DEBUG,  # Можно заменить на другой уровень логгирования.
                    )

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "botni ishga tushuriish"),
            types.BotCommand("help", "bot haqida malumot"),
            types.BotCommand("rek", "Botimizda Reklama bermoqchimisiz"),
        ]
    )

@dp.message_handler(commands="start")
async def Start(mes:types.Message):
    await mes.answer(f"Assalomu Alaykum {mes.from_user.first_name}!! Bizning Botimizga hush kelibsiz!! bot haqida malumot olish uchun /help komandasini bosing!!",reply_markup=button)
    registeruser(f"{mes.from_user.username}",f"{mes.from_user.first_name}",f"{mes.from_user.id}")
@dp.message_handler(text="Fikir bildiring")
async def forfeedback(message:types.Message):
    await message.answer(f"{message.from_user.first_name} Botga habar matnini yuboring shunda u ushbu bo egasi va dasturchisi Muhiddinov Abdulhodiyga yetib boradi Yaxshi Fikringiz uchun tashakkur")
    await Feedstate.Text.set()
@dp.message_handler(state=Feedstate.Text)
async def ForFeedBack(message:types.Message,state:FSMContext):
    await message.answer(f" Tabriklayman {message.from_user.first_name} Fikringiz Dasturchiga Yuborildi",feedback(f"{message.from_user.id}",f"{message.text}"))
    await state.finish()



@dp.message_handler(commands="rek")
async def Reklama(message:types.Message):
    await message.answer("Assalomu Alaykum siz Reklama bermoqchimisiz Yoki Telegram Bot Kerakmi? \n una bizbilan boglaning \n Ism: Abdulhodiy \n Telegram @Muhiddinov2004 \n Tel: +998904069233")

@dp.message_handler(commands="help")
async def start(message: types.Message):
    await message.answer(
        text=f"""Assalomu Alaykum {message.from_user.first_name}
  \n Bizning botimizning maqsadi sizga  siz kabi Telegram foydalanuvchilariga
  \n ishtimoi tarmoqlardan video va rasmlarni yuklab berish 
  \n Hozircha biz faqat YouTube dan shorts video va rasmlarni Yuklay olamiz
  \n bot:@PANTERA_DOWNLOADE_bot 
  \n Version:0.0.01, 
  \n Yangilanish muddati 1 Oydan Song!!""")

# Assalomu Alaykum Abdulhodiy
#  Bizning botimizning maqsadi sizga  siz kabi Telegram foydalanuvchilariga
#  ishtimoi tarmoqlardan video va rasmlarni yuklab berish
#  Hozircha biz faqat YouTube dan shorts video va rasmlarni Yuklay olamiz
#  bot:@PANTERA_DOWNLOADE_bot
#  Version:0.0.01, Yangilanish muddati 1 Oydan Song!!
def video_yuklash_va_malumot_aniqlash(url):
    video_id = url.split('/')[-1].split('?')[0]  # Video manzilidan videoning ID sini ajratib olamiz
    yuklash_url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
    querystring = {"id": video_id}
    headers = {
        "X-RapidAPI-Key": "e3684610b3msh79b163477bf1d96p115985jsn539529554741",
        "X-RapidAPI-Host": "ytstream-download-youtube-videos.p.rapidapi.com"
    }

    response = requests.get(yuklash_url, headers=headers, params=querystring)
    res = response.json()

    title = res["title"]
    view_count = res['viewCount']
    description = res["description"]
    channel_title = res['channelTitle']
    thumbnail_url = res["thumbnail"][0]["url"]
    audio_url = res['formats'][0]['url']
    video_urls = res['formats'][2]['url']

    return title, view_count, description, channel_title, thumbnail_url, audio_url, video_urls


@dp.message_handler(regexp=r'(https?://)?(www\.)?youtube\.com/shorts/(\S+)' or r"(https?://)?(www\.)?youtu\.be/(\S+)")
async def youtube_url_qabul_qilish(message: types.Message):
    url = message.text.strip()
    title, view_count, description, channel_title, thumbnail_url, audio_url, video_urls = video_yuklash_va_malumot_aniqlash(
        url)

    # Endi ushbu o'zgaruvchilarni foydalanish orqali, misol uchun foydalanuvchiga javob sifatida yuborish mumkin:
    javob_xabari = f"Sarlavha: {title}\nKo'rishlar soni: {view_count}\nTavsif: {description}\nKanal sarlavhasi: {channel_title}"
    await message.reply(javob_xabari)
    await bot.send_video(message.from_user.id, video_urls)


# async def on_startup(dp):

async def on_startup(dispatcher):
    # komandalar
    await bot.send_message(chat_id='5640990557', text='Bot ishga tushirildi va ishlayapti!')
    await set_default_commands(dispatcher)
    # bot ishga tushdi yoki adminga habar
    # await on_startup_notify(dispatcher)

#@dp.message_handler()
#async def Instagram(message:types.Message):
#    if message.text == "https://www.instagram.com/p/" or "https://www.instagram.com/":
#        link=f"{message.text}"

#        url = "https://instagram-story-downloader-media-downloader.p.rapidapi.com/index"

#        querystring = {"url": link}

#        headers = {
#            "X-RapidAPI-Key": "e3684610b3msh79b163477bf1d96p115985jsn539529554741",
#            "X-RapidAPI-Host": "instagram-story-downloader-media-downloader.p.rapidapi.com"
#        }
#
#        response = requests.get(url, headers=headers, params=querystring)
#        try:
#            insta=INSTAGRAM(link)
#            await bot.send_video(message.chat.id,video=insta)
#        except TypeError as e:
#            res = response.json()
#            for video in video:
#                await bot.send_video(message.chat.id,video=video)



if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

