import telegram
import asyncio
import schedule
import time
import pytz
import datetime

async def send_telegram_message():
    token = "6898150295:AAE8hxjfg3rQuGPzuEuwHPLNExqlZ3yAWKs"
    bot = telegram.Bot(token=token)
    public_chat_name = '@opensw2023'

    now = datetime.datetime.now(pytz.timezone('Asia/Seoul'))
    if now.hour >= 23 or now.hour <= 6:
        return


    message = await bot.send_message(chat_id=public_chat_name, text="30분 경과")
    id_channel = message.chat.id
    print(f"Sent message to chat ID: {id_channel}") #텔레그렘에 나옴

def job():
    print("수행 완료") #콘솔창에 나오게 함
    asyncio.run(send_telegram_message())

    


schedule.every(30).minutes.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
