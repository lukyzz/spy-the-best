import pyautogui
import time
import requests
import telegram



def telegram_and_screenshot():
    i = 1
    while i<6:
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'<PATH-ONDE-VAI-SALVAR-IMAGEM>')
        TELEGRAM_BOT_TOKEN = '<SEUTOKEN>'
        TELEGRAM_CHAT_ID = '<-CHATID>'
        PHOTO_PATH = '<PATH-ONDE-IMAGEM-ESTA SALVA>'

        bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="From Telegram Bot")

        bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb'))

        time.sleep(20)

    i += 1

telegram_and_screenshot()

