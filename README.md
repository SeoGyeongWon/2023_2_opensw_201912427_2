# 2023_2_opensw_201912427_2 

2. 텔레그램 봇 과제 제출

   <img width="960" alt="시간정지" src="https://github.com/SeoGyeongWon/2023_2_opensw_201912427_2/assets/126853734/1727663b-c01c-43c4-a4bf-bde469df20d1">


실행 결과가 30분에 한번씩 알람이 오게하는것과 23시부터 6시까지는 알람이 오지 못하게 하는것인데 시간 간격의 텀이 길다고 느껴,<br/>
실행시 알람이 오는주기는 1분, 알람이 오지못하게 하는 시간은 03:20 ~ 03:23으로 설정해두어 실행결과를 만들어냈습니다.<br/>
같은 코드에서 시간 주기만 바꾼것이기에 알람이 오는 주기를 30분으로 바꾸고 알람이 오지 못하게 설정하는 시간대를 23시부터 06시까지로 해두어도 원하는 결과가 나올것입니다.<br/><br/>

업로드한 실행 코드는 알람 주기 30분 알람 오지 못하게 하는 시간대 23시부터 06시로 수정해서 올렸습니다.<br/>

수업 자료에 있었던 채널메시지 보내기<br/>

import telegram<br/>
token = ""<br/>
bot = telegram.Bot(token = token)<br/>
public_chat_name = '@K2022_2_test'<br/>
id_channel = bot.sendMessage(chat_id=public_chat_name, <br/>
text="alarm arrived!!!!!").chat_id<br/>
print(id_channel)<br/>

해당 코드를 실행시<br/>

File "c:\Users\skwkn\OneDrive\바탕 화면\대학\3-2 학기\오픈소스sw\텔레그램 봇\1.py", line 7, in <module>      
    text="alarm arrived!!!!!").chat_id
                               ^^^^^^^
AttributeError: 'coroutine' object has no attribute 'chat_id'
sys:1: RuntimeWarning: coroutine 'Bot.send_message' was never awaited <br/><br/>

이와 같은 오류가 발생하였습니다. 

sendMessage 메서드에 오류가 있는것으로 확인됬으며, 비동기가 제대로 이루어지지 않은것 같습니다.<br/>
이에 async def를 사용하여 비동기 함수를 정의하고 await를 사용하여 비동기적으로 실행될 수 있도록 수정했습니다.
